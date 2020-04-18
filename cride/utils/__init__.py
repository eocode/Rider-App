"""Django models utilities"""

# Django
from django.db import models


class CRideModel(models.Model):
    """Comparte Ride base model
    CRide Model acts as an abstract base class from which every
    other model in the prohect will inherit. This class provides
    every table with the following attributes:
        + created (Datetime): Store the datetime the object was created
        + modified (Datetime): Store the last datetime the object was modified
    """

    created = models.DateTimeField(
        'created_at',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )

    modified = models.DateTimeField(
        'modified_at',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )

    class Meta:
        """Meta option"""

        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']


# Proxy models, extienden el comportamiento
# class Student(CRideModel):
#     name = models.CharField()

#     class Meta(CRideModel.Meta):
#         db_table = 'student_role'

# class Person(models.Model):
#     first_name = models.CharField()
#     last_name = models.CharField()

# class MyPerson(Person):
#     class Meta:
#         proxy = True

#     def say_hi(name):
#         pass

# MyPerson.objects.all()
# ricardo = MyPerson.object.get(pk=1)
# ricardo.say_hi('Pablo')
