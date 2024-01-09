from django.urls import path
from .views import ReceberNome

urlpatterns = [
    path("name/", ReceberNome.as_view()),
]
