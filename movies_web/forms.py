from django.forms import ModelForm
from movies_web.models import Movie, AdditionalInfo


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'description', 'premiere', 'imdb_rating', 'poster']


class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ['czas_trwania', 'gatunek']
