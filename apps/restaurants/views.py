from rest_framework.viewsets import ModelViewSet

from apps.restaurants.models import Restaurant
from apps.restaurants.serializers import RestaurantSerializer


class RestaurantApiViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    #код для отображения карты

    # def list(self, request, *args, **kwargs):
    #     locations = Restaurant.objects.all()
    #     m = folium.Map(location=[51.5070, -0.1270], zoom_start=10)
    #     for location in locations:
    #         folium.Marker([location.latitude, location.longitude], popup=location.title).add_to(m)
    #     return HttpResponse(m._repr_html_())
