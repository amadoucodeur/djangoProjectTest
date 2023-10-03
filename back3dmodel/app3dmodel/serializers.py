from rest_framework import serializers
from .models import Model3d, Badge, UserProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ('id', 'name', 'description')

class UserProfileSerializer(serializers.ModelSerializer):
    account = UserSerializer()
    badges = BadgeSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'account', 'badges')

class Model3dSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Model3d
        fields = ('id', 'user', 'name', 'image', 'views')
