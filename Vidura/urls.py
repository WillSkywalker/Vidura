from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from Vidura.webapp import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r've_vg_food', views.VegetarianVeganFoodViewSet, basename='ve_vg_food')
router.register(r'food', views.FoodViewSet, basename='food')
router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
