from django.shortcuts import render
from .models import Main
import json
from django.http import HttpResponse
# import pandas as pd

def ccc(request):
    # print("hoge")
    # return HttpResponse("ハローワールド")

    if request.method == "GET":
            if "day_button" in request.GET:

                print("through day button")
                return HttpResponse("ハローワールド")
            elif "week_button" in request.GET:
                print("GET week button")

            elif "month_button" in request.GET:
                print("GET month_button")

            elif "year_button" in request.GET:
                print("GET year_button")
            else:
                return HttpResponse("ハローワールド")