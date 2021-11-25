from django.shortcuts import render
from django.http import HttpResponse


def index_response(request):
    return HttpResponse('<h1> Filmy z sieci </h1>')
