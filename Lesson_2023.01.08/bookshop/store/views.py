from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Rating
from random import randint


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_random_rating(request, book_id):
    random_vote = randint(1, 5)
    book = Book.objects.get(pk=book_id)
    # q.choice_set.create(choice_text='Not much', votes=0)
    return HttpResponse(f"You're added rating {'★'*random_vote}{'☆'*(5-random_vote)} for {book}")

def results(request, book_id):
    return HttpResponse(f"You're looking at the results of item {book_id}")
