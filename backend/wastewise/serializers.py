from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.user import User
from .models.spot import Spot
from .models.item import Item

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = { 'password': {'write_only': True, 'min_length': 5}}
    
    # create user
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

# User signup validation
class UserRegisterSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    # validate user signup form
    def validate(self, data):
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Make sure to enter a password and password confirmation.')
        
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Oops! Passwords don/"t match')
        
        return data

# Spot serializers
class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = '__all__'

class SpotReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = '__all__'

class SpotWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = '__all__'

# Item serializers
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'