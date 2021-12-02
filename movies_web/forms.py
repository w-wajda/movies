from django.forms import ModelForm
from movies_web.models import Movie, AdditionalInfo, Rating, Actor


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'description', 'premiere', 'imdb_rating', 'poster']


class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ['czas_trwania', 'gatunek']


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['gwiazdki', 'recenzja']


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['imie', 'nazwisko']
