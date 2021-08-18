from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserActivity


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class UserActivSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserActivity
        fields = ('id', 'user', 'start_of_activity', 'end_of_activity', 'type_active', 'distance', 'calorie_count',)


class CreateActivSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ('id', 'start_of_activity', 'end_of_activity', 'type_active', 'distance', 'calorie_count',)
