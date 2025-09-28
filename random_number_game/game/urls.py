from django.contrib import admin
from django.urls import path,include
from game import views

urlpatterns = [
    path("",views.game_view,name="game"),
    #path("api/",views.ga)
]