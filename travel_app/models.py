from django.db import models
from django.contrib.auth.models import User

class TravelPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    budget = models.IntegerField()

    PLACE_CHOICES = [
        ('Hill', 'Hill'),
        ('Mountain', 'Mountain'),
        ('Beach', 'Beach'),
        ('Forest', 'Forest'),
        ('Temple', 'Temple'),
        ('Historical', 'Historical'),
        ('Adventure', 'Adventure'),
    ]

    WEATHER_CHOICES = [
        ('Cool', 'Cool'),
        ('Hot', 'Hot'),
    ]

    place_type = models.CharField(max_length=20, choices=PLACE_CHOICES)

    weather = models.CharField(max_length=20, choices=WEATHER_CHOICES)

    days = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username