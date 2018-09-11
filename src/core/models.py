"""
core models , can be shared by other apps.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser

from .options import ROLES


class Role(models.Model):
    """
    to store roles available
    """
    id = models.PositiveSmallIntegerField(choices=ROLES.CHOICES,
            primary_key=True)

    def __str__(self):
        """
        to return role name
        """
        return self.get_id_display()


class User(AbstractUser):
    """
    Users within the Django authentication system
    are represented by this model.
    """
    roles = models.ManyToManyField(Role)
