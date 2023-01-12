from django.contrib import admin

from .models import Item, UserRating

admin.site.register(Item)
admin.site.register(UserRating)

# Register your models here.
