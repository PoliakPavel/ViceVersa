from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('<h1><center>This is about page<center><h1>')


def home(request):
    return render(request, 'home.html', {'greeting': "Hello"})


def reverse(request):
    user_text = request.GET['user_text']
    reversed_text = user_text[::-1]
    words = user_text.split()
    number_of_words = len(words)
    return render(request, 'reverse.html', {'user_text': user_text, 'reversed_text': reversed_text,
                                            'number_of_words': number_of_words})
