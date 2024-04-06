from django.db import models

from apps.restaurants.models import Restaurant


class Review(models.Model):
    """
    Model for reviews
    """
    CHOICES_STAR = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    username = models.CharField(
        max_length=256,
        verbose_name='username'
    )
    comment = models.TextField(
        verbose_name='comment'
    )
    star = models.IntegerField(
        choices=CHOICES_STAR,
        verbose_name='star'
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant',
        verbose_name='restaurant'
    )

    def __str__(self) -> str:
        return f'{self.id} -- {self.username}'
    
    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'Reviews'
