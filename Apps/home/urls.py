from django.contrib import admin
from django.urls import path, include
from Apps.home.views import homeView

app_name = 'home'

urlpatterns = [
    path('', homeView.as_view(), name='home'),
]
