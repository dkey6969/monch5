from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.is_active = False
        user.generate_confirmation_code()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError("Неверные данные для входа.")
        if not user.is_active:
            raise serializers.ValidationError("Аккаунт не активирован.")
        return user


class ConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    def validate(self, data):
        try:
            user = CustomUser.objects.get(username=data['username'])
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Пользователь не найден.")

        if user.confirmation_code != data['confirmation_code']:
            raise serializers.ValidationError("Неверный код подтверждения.")

        return data

    def save(self, **kwargs):
        user = CustomUser.objects.get(username=self.validated_data['username'])
        user.is_active = True
        user.confirmation_code = None
        user.save()
        return user