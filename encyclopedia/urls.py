from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entries/<str:name>", views.entry, name="entry"),
    path("add", views.add, name="add"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("results", views.search, name="search"),
    path("random", views.random_page, name="random")
]
