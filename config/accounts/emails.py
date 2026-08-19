from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse



def send_verification_email(user, uid, token):
    verification_path = reverse(
        "verify-email",
        kwargs = {
            "uid": uid,
            "token": token,
        },
    )

    verification_url = (
        f"http://127.0.0.1:8000{verification_path}"
    )

    subject = "Verify your email address"

    message = f"""
Hello {user.first_name},

Thank you for registering.

Please click the link below to verify your email address:

{verification_url}

If you did not create this account, you can safely ignore this email.

Regards,
Authentication API Team
"""

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )