from django.shortcuts import render
from .models import Main
import json
import datetime

def month_button(request):
    template_name = 'twitter_analysis/index.html'
    labels = []
    data = []
    context ={}
    today = datetime.date.today()

    # lt = less than (not contain today), gte = greater than equal (contain the day)
    queryset = Main.objects.filter(date__lt=today, date__gte=(today + datetime.timedelta(-30)))
    for record in queryset:
        labels.append(record.date)
        data.append(record.average_polality)

    var = {
        'labels': labels,
        'data': data,
    }

    context = {'data_json':json.dumps(var, default=str)}
    print("GET week button")

    return render(request, template_name, context)
