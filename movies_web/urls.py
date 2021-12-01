from django.urls import path
from movies_web.views import main_movies, \
    create_movie, \
    update_movie, \
    delete_movie

urlpatterns = [
    path('main/', main_movies, name='main_movies'),
    path('new/', create_movie, name='create_movie'),
    path('edit/<int:id>/', update_movie, name='update_movie'),
    path('delete/<int:id>/', delete_movie, name='delete_movie'),
]
