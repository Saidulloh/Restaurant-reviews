from django.db import models
# from django.contrib.gis.db import models


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
    def __str__(self) -> str:
        return f'{self.id} -- {self.title}'
    
    class Meta:
        verbose_name = 'restaurant'
        verbose_name_plural = 'Restaurants'
