from rest_framework.routers import DefaultRouter

from apps.restaurants.views import RestaurantApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=RestaurantApiViewSet
)

urlpatterns = router.urls
