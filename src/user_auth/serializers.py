from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, style={"input_type": "password", "placeholder": "Password"}
    )
    password2 = serializers.CharField(
        write_only=True,
        style={"input_type": "password", "placeholder": "Confirm Password"},
    )
    username = serializers.CharField(
        style={"placeholder": "Username", "autofocus": True}
    )

    class Meta:
        model = User
        fields = ("username", "password", "password2")

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150, style={"placeholder": "Username", "autofocus": True}
    )
    password = serializers.CharField(
        max_length=128, style={"input_type": "password", "placeholder": "Password"}
    )

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        data["user"] = user
        return data
