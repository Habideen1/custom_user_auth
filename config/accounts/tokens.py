from django.contrib.auth.tokens import  PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    """
    Generates and validates secure tokens used
    for email verification.
    """


    def _make_hash_value(self, user, timestamp):
        return(
            str(user.pk)
            + str(timestamp)
            + str(user.is_active)
        )

email_verification_token = EmailVerificationTokenGenerator()


