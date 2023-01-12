from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    numbers = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.book
