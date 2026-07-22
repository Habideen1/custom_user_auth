from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password



User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User

    fields = (
        "id",
        "email",
        "first_name",
        "last_name",
        "password",
        "password_confirm",
    )

    extra_kwargs = {
        "password": {
            "write_only": True
        }
    }

    
    def validate_password(self, value):
        validate_password(value)
        return value
    


    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError(
                {
                    "password_confirm": "Passwords do not match."
                }
            )
        return attrs
        
    
    def create(self, validated_data):
        validated_data.pop("password_confirm")

        user = User.objects.create_user(**validated_data)

        return user