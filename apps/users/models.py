from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.NumberValidator import kg_phone_validator


class User(AbstractUser):
    """
    Model for users
    """
    username = models.CharField(
        unique=True,
        max_length=255,
        verbose_name='username'
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name='first_name'
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name='last_name'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='email'
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[kg_phone_validator],
        verbose_name='phone_number'
    )
    created_at = models.DateTimeField( 
        auto_now_add=True,
        verbose_name='created_at'
    )

    def __str__(self):
        return f'{self.id} -- {self.username}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Users'
