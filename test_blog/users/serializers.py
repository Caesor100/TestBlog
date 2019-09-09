from rest_framework import serializers


class UserProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    id = serializers.IntegerField()


class UserNameSerializer(serializers.Serializer):
    username = serializers.CharField()
