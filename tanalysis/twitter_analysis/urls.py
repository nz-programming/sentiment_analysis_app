from django.urls import path
from . import views
from . import views_week_button
from . import views_month_button
from . import views_year_button


urlpatterns = [
    path('', views.index, name='index'),
    path('week', views_week_button.week_button, name='index'),
    path('month', views_month_button.month_button, name='index'),
    path('year', views_year_button.year_button, name='index'),
]