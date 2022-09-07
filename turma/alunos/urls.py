from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro", views.cadastro, name="cadastro"),
    path("<int:id>/edit", views.edit, name="edit"),
]