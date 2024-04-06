from django.contrib import admin

from apps.restaurants.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
