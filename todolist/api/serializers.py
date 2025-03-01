from rest_framework import serializers
from .models import User, Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'age', 'created_at']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'image']

def validate_phone_number(self, value):
    if not value.startswith('+996'):
        raise serializers.ValidationError("Номер телефона должен начинаться с +996")
    return value