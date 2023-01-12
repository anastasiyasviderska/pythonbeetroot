from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    numbers = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class UserRating(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.item


