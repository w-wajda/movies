from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from movies_web.models import Movie, AdditionalInfo, Rating, Actor
from movies_web.forms import MovieForm, AdditionalInfoForm, RatingForm, ActorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from movies_web.serializers import UserSerializer, MovieSerializer

from rest_framework import viewsets


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


def main_movies(request):
    all_movies = Movie.objects.all()
    return render(request, 'main.html', {'movies': all_movies})


@login_required
def create_movie(request):
    form_movie = MovieForm(request.POST or None, request.FILES or None)
    form_additional = AdditionalInfoForm(request.POST or None)

    if form_movie.is_valid() and form_additional.is_valid():
        movie = form_movie.save(commit=False)
        additional = form_additional.save()
        movie.dodatkowe = additional
        movie.save()

        return redirect(main_movies)

    return render(request, 'form_movie.html', {'form': form_movie, 'form_additional': form_additional, 'new': True})


@login_required
def details_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    ratings = Rating.objects.filter(film=movie)

    form_rating = RatingForm(request.POST or None)

    if request.method == 'POST':
        if 'gwiazdki' in request.POST:
            rating = form_rating.save(commit=False)
            rating.film = movie
            rating.save()

    return render(request, 'details_movie.html', {'movie': movie, 'ratings': ratings, 'form_rating': form_rating})


@login_required
def update_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    try:
        additional = AdditionalInfo.objects.get(movie=movie.id)
    except AdditionalInfo.DoesNotExist:
        additional = None

    form_movie = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    form_additional = AdditionalInfoForm(request.POST or None, instance=additional)

    if form_movie.is_valid() and form_additional.is_valid():
        movie = form_movie.save(commit=False)
        additional = form_additional.save()
        movie.dodatkowe = additional
        movie.save()

    return render(request, 'form_movie.html', {'form': form_movie, 'form_additional': form_additional, 'new': False})


@login_required
def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
        movie.delete()
        return redirect(main_movies)

    return render(request, 'delete_movie.html', {'movie': movie})
