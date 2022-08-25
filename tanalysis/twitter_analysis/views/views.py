from django.shortcuts import render
from ..models import Main
import json
from ..config.config import create_dataset

def index(request):
    queryset = Main.objects.all()
    template_name, dataset = create_dataset(queryset)
    return render(request, template_name, dataset)