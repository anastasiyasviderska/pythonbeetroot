from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, UserRating
from random import randint


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_random_rating(request, item_id):
    random_vote = randint(1, 5)
    book = Item.objects.get(pk=item_id)
    # q.choice_set.create(choice_text='Not much', votes=0)
    return HttpResponse("You're looking at item %s." % book)

def results(request, item_id):
    response = "You're looking at the results of item %s."
    return HttpResponse(response % item_id)
