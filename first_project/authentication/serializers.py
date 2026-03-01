from rest_framework import serializers
from .models import Author
from django.contrib.auth.password_validation import validate_password


class AuthorSignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Author
        fields = (
            "image",
            "username",
            "email",
            "subtitle",
            "bio",
            "password1",
            "password2",
        )

    def validate(self, data):
        password1 = data.get("password1")
        password2 = data.get("password2")

        if password1 != password2:
            serializers.ValidationError({"password2": "Passwords are not the same."})
        validate_password(password=password1)

        return data

    def create(self, validated_data):
        password = validated_data.pop("password1")
        validated_data.pop("password2")
        user = Author.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
