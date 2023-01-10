from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=200)
    numbers = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

class UserRating(models.Model):
    item = Items
    user_rating = models.FloatField(default=0.0)


