from django.urls import path
from rest_framework.routers import DefaultRouter

from store.apps import StoreConfig
from store.views import CartAPI, CategoryViewSet, ProductViewSet

app_name = StoreConfig.name

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path("cart/", CartAPI.as_view(), name="cart"),
] + router.urls
