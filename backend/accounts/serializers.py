from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['id', 'email', 'full_name', 'role']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'role', 'password']

        def create(self, validated_date):
            user = User(
                email = validated_date['email'],
                full_name = validated_date['full_name'],
                role = validated_date['role'],
            )
            user.set_password(validated_date['password'])
            user.save()
            return user
