from django.urls import path, include
from rest_framework import routers

from apiV2.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

app_name = 'apiV2'
urlpatterns = [
    path('', include(router.urls)),
]