from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def good_morning(request):
    date=datetime.datetime.now()
    s='<h1>Hi, Good morning, the date and time from the server is:'+str(date)+'</h1>'
    return HttpResponse(s)
