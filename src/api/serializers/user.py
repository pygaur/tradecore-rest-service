"""
user serializers
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        """
        """
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password')

    def encrypt_password(self, validated_data):
        """
        encrypt password.
        """
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        return validated_data

    def create(self, validated_data):
        """
        encrypt password before .
        """
        validated_data = self.encrypt_password(validated_data)
        return super(UserSerializer, self).create(validated_data)
