from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Rating
from random import randint


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_random_rating(request, book_id):
    random_vote = randint(1, 5)
    book = Book.objects.get(pk=book_id)
    book.rating_set.create(user_rating=random_vote)
    return HttpResponse(f"You're added rating {'★'*random_vote}{'☆'*(5-random_vote)} for {book}")

def results(request, book_id):
    book = Book.objects.get(pk=book_id)
    ratings = list(book.rating_set.all())
    ratings_star = map(lambda x: f"{'★'*x.user_rating}{'☆'*(5-x.user_rating)}", ratings) 
    return HttpResponse(f'You\'re looking at the results of item {book}: {", ".join(ratings_star)}')
