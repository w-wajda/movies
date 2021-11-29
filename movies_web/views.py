from django.shortcuts import render, get_object_or_404, redirect
from movies_web.models import Movie
from movies_web.forms import MovieForm
from django.contrib.auth.decorators import login_required


def index_movies(request):
    all_movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': all_movies})


@login_required
def create_movie(request):
    form = MovieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(index_movies)

    return render(request, 'form_movie.html', {'form': form})


@login_required
def update_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)

    if form.is_valid():
        form.save()
        return redirect(index_movies)

    return render(request, 'form_movie.html', {'form': form})


@login_required
def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
        movie.delete()
        return redirect(index_movies)

    return render(request, 'confirm_movie.html', {'movie': movie})