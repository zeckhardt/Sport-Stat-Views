"""
URL configuration for sportStatTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sportStatTracker import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nfl/player', views.input_nfl_player, name='nfl_player'),
    path('nfl/visualize/', views.nfl_player_visualize, name='nfl_player_visualize'),
    path('nba/player', views.input_nba_player, name='nba_player'),
    path('nba/visualize/', views.nba_player_visualize, name='nba_player_visualize'),
]
