from django.shortcuts import render
from .models import Main
import json
import datetime

def week_button(request):
    template_name = 'twitter_analysis/index.html'
    labels = []
    average_polality = []
    context ={}
    today = datetime.date.today()

    # lt = less than (not contain today), gte = greater than equal (contain the day)
    queryset = Main.objects.filter(date__lt=today, date__gte=(today + datetime.timedelta(-7)))
    for record in queryset:
        labels.append(record.date)
        average_polality.append(record.average_polality)

    var = {
        'labels': labels,
        'average_polality': average_polality,
    }

    context = {'data_json':json.dumps(var, default=str)}
    print("GET week button")

    return render(request, template_name, context)
