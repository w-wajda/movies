from django.forms import ModelForm
from movies_web.models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'description', 'premiere', 'imdb_rating', 'poster']