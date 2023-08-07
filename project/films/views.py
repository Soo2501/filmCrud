from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
# Create your views here.

def show(request):
    return render(request,"films/film_list.html")

class FilmBaseView(View):
    model = Film
    fields = "__all__"
    success_url = reverse_lazy("films:film-list")

class FilmListView(FilmBaseView, ListView):
    """View to list all films.
    Use the 'film_list' variable in the template
    to access all Film objects"""

class FilmDetailView(FilmBaseView, DetailView):
    """View to list the details from one film.
    Use the 'film' variable in the template to access
    the specific film here and in the Views below"""

class FilmAddView(FilmBaseView, CreateView):
    """View to create a new film"""

class FilmEditView(FilmBaseView, UpdateView):
     """View to update a film"""

class FilmDeleteView(FilmBaseView, DeleteView):
    """View to delete a film"""

    
