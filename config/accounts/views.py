from django.contrib.auth import get_user_model
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import CreateAPIView

from .emails import send_verification_email
from .serializers import RegisterSerializer, LoginSerializer
from .tokens import email_verification_token
from rest_framework_simplejwt.tokens import RefreshToken 



User = get_user_model()

class RegisterAPIView(CreateAPIView):
    serializer_class =  RegisterSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        
        user = serializer.save()

        uid = urlsafe_base64_encode(
            force_bytes(user.pk)
        )

        token = email_verification_token.make_token(user)

        send_verification_email(
            user=user,
            uid=uid,
            token=token,
        )

        return Response(
            {
                "message": (
                    "Registration successful."
                    "Please check your email to verify your account."
                ),
                "user": {
                    "id": str(user.id),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
            },
            status=status.HTTP_201_CREATED,
        )

    

class VerifyEmailAPIView(APIView):
    def get(self, request, uid, token):
        try:
            uid= force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response(
                {
                    "message": "Invalid verification link."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if user.is_active:
            return Response(
                {
                    "message": "Email has already been verified."
                },
                status=status.HTTP_200_OK,
            )

        if not email_verification_token.check_token(user, token):
            return Response(
                {
                    "message": "Verification link is invalid or expired."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.is_active = True
        user.save(update_fields=["is_active"])

        return Response(
            {
                "message": "Email verified successfully. "
                "Your account is now active."
            },
             status=status.HTTP_200_OK,
        )



class LoginAPIView(APIView):
    def post(slf, request):
        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": "Login successful.",
                "user": {
                    "id": str(user.id),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
            },
            status=status.HTTP_200_OK,
        )
