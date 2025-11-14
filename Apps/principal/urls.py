from django.contrib import admin
from django.urls import path, include
from Apps.principal.views import principalView, productosView

app_name = 'principal'

urlpatterns = [
    path('', principalView.as_view(), name='principal'),
    path('productos/', productosView.as_view(), name='productos'),
]
