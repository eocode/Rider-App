"""Circles URLs"""

# Django
from django.urls import  path

# views
from cride.circles.views import list_circles

urlpatterns = [
    path('circles/', list_circles)
]

