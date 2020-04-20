"""Circles serializers"""
# Django REST Framework
from rest_framework import serializers

# Model
from cride.circles.models import Circle

class CircleModelSerializer(serializers.ModelSerializer):
    """Circle model serializer"""

    class Meta:
        """Meta class."""

        model = Circle
        fields = (
            'id', 'name', 'slug_name',
            'about', 'picture', 'rides_taken',
            'verified', 'is_public',
            'is_limited', 'members_limit'
        )
