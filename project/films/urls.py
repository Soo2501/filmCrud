from django.urls import path
from .views import *

app_name = "films"

urlpatterns = [
    # path("", show, name="film-list"),
    path("", FilmListView.as_view(), name="film-list"),
    path("films/<int:pk>/detail", FilmDetailView.as_view(), name="film-detail"),
    path("films/add/", FilmAddView.as_view(), name="add-film"),
    path("films/<int:pk>/edit/", FilmEditView.as_view(), name="edit-film"),
    path("films/<int:pk>/delete/", FilmDeleteView.as_view(), name="delete-film"),
]