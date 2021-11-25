from django.urls import path
from movies_web.views import index_response

urlpatterns = [
    path('index/', index_response)
]
