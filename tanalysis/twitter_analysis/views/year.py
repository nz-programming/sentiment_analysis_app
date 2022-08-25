from ..config.config import *
from django.shortcuts import render
from ..models import Main
import datetime
from .common.common import create_dataset

def year_button(request):
    queryset = Main.objects.filter(date__lt=TODAY, date__gte=(TODAY - SHOW_PERIOD_YEAR))
    template_name, dataset = create_dataset(queryset)
    return render(request, template_name, dataset)
