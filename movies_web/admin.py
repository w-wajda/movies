from django.contrib import admin
from movies_web.models import Movie, AdditionalInfo, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'imdb_rating']
    list_filter = ['title', 'year']
    search_fields = ['title', 'description']


admin.site.register(AdditionalInfo)
admin.site.register(Rating)
