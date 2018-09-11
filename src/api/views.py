"""
api views
"""
from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import generics

from user.models import Account
from .serializers import UserSerializer

User = get_user_model()


class UserView(generics.CreateAPIView):
    """
    User Signup
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        """
        to save extra user's Account data.
        """
        with transaction.atomic():
            super(UserView, self).perform_create(serializer)    
            user = serializer.instance            
            Account.objects.create(user=user)
