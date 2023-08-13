from django.contrib import admin
from django.urls import path, include

from characters.views import get_random_character_view, CharacterListView

urlpatterns = [
    path("characters/", CharacterListView.as_view(), name="character-list"),
    path("characters/random/", get_random_character_view, name="character-random"),
]

app_name = "characters"
