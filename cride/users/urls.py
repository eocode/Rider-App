"""Users URLs"""

# Django
from django.urls import  path

# views
from cride.users.views import UserLoginAPIView

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
]



