from django.urls import path
from movies_web.views import index_movies

urlpatterns = [
    path('index/', index_movies)
]
