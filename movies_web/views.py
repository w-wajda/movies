from django.shortcuts import render
from django.http import HttpResponse
from movies_web.models import Movie


def index_movies(request):
    # return HttpResponse('<h1> Filmy z sieci </h1>')
    all_movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': all_movies})
