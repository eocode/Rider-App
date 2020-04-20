"""Circles URLs"""

# Django
from django.urls import include, path

# Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import circles as circle_views

router = DefaultRouter()
router.register(r'circles', circle_views.CircleViewSet, basename='circle')

urlpatterns = [
    path('', include(router.urls))
]

