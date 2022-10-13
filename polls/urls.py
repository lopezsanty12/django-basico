from django.urls import path
from . import views

app_name = "polls"  # es el nombe de la app es importante para usar en las vista html
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/detail/5/
    path("detail/<int:pk>", views.DetailView.as_view(), name="detail"),
    # ex: /polls/results/5/
    path("results/<int:pk>", views.ResultsView.as_view(), name="results"),
    # ex: /polls/vote/5/
    path("vote/<int:question_id>", views.vote, name="vote"),
]