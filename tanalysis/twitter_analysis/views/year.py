from django.shortcuts import render
from ..models import Main
import datetime
from .common.common import create_dataset

def year_button(request):
    queryset = Main.objects.filter(date__lt=datetime.date.today(), date__gte=(datetime.date.today() + datetime.timedelta(-365)))
    template_name, dataset = create_dataset(queryset)
    return render(request, template_name, dataset)
