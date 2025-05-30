from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:heroes_id>/", views.detail, name="detail"),
    path("<int:heroes_id>/results/", views.results, name="results"),
    path("<int:heroes_id>/vote/", views.vote, name="vote"),
]