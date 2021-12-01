from django.contrib import admin
from movies_web.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'imdb_rating']
    list_filter = ['title', 'year']
    search_fields = ['title', 'description']