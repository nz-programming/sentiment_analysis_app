from django.urls import path
from .views import views
from .views import week
from .views import month
from .views import year


urlpatterns = [
    path('', views.index, name='index'),
    path('week', week.week_button, name='index'),
    path('month', month.month_button, name='index'),
    path('year', year.year_button, name='index'),
]