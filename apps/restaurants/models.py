from django.db import models
# from django.contrib.gis.db import models

from apps.users.models import User


class Restaurant(models.Model):
    """
    Model for restaurants
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    latitude = models.FloatField(
        verbose_name='latitude'
    )
    longitude = models.FloatField(
        verbose_name='longitude'
    )
    description = models.TextField(
        verbose_name='description'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='restaurant_owner',
        verbose_name='restaurant_owner'
    )

    def __str__(self) -> str:
        return f'{self.id} -- {self.title}'
    
    class Meta:
        verbose_name = 'restaurant'
        verbose_name_plural = 'Restaurants'
