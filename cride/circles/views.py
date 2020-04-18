"""Circles views"""

# Django
from django.http import JsonResponse

# Models
from cride.circles.models import Circle

def list_circles(request):
    """List circles"""
    circles = Circle.objects.all()
    public = circles.filter(is_public=True)
    data = []
    for circle in public:
        data.append({
            'name': circle.name,
            'slug_name': circle.slug_name,
            'rides_taken': circle.rides_taken
        })
    return JsonResponse(data, safe=False)
