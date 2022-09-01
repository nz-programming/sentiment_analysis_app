from ..config.config import *
from django.shortcuts import render
from ..models import Main
from .common.common import create_dataset

def month_button(request):
    queryset = Main.objects.filter(date__lte=TODAY, date__gte=(TODAY - SHOW_PERIOD_MONTH))
    template_name, dataset = create_dataset(queryset)
    return render(request, template_name, dataset)
