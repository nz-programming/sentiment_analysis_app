from django.urls import path
from . import views
from . import views_copy


urlpatterns = [
    path('', views.index, name='index'),
    path('bbb', views_copy.ccc, name='index'),
]