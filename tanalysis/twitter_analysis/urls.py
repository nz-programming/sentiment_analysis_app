from django.urls import path
from . import views


urlpatterns = [
    path('', views.gorira, name='index'),
]