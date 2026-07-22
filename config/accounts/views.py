from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView

from .serializers import RegisterSerializer



class RegisterAPIView(CreateAPIView):
    serializer_class =  RegisterSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        
        user = serializer.save()

        return Response(
            {
                "message": "User registered successfully.",
                "user": {
                    "id": str(user.id),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
            },
            status=status.HTTP_201_CREATED,
        )






