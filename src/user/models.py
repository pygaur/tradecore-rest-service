"""
models required for users.
"""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Account(models.Model):
    """
    to store account details of the user.
    mapped with 1to1 with User Model.
    """
    user = models.OneToOneField(User, primary_key=True,
                                on_delete=models.CASCADE)

    class Meta:
        app_label = "user"
