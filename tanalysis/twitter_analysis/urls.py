from .config.config import *
from django.urls import path
from .views import views
from .views import week
from .views import month
from .views import year


urlpatterns = [
    path('', views.index, name = PATH_INDEX),
    path(PATH_WEEKBUTTON, week.week_button, name = PATH_WEEKBUTTON),
    path(PATH_MONTHBUTTON, month.month_button, name = PATH_MONTHBUTTON),
    path(PATH_YEARBUTTON, year.year_button, name = PATH_YEARBUTTON),
]