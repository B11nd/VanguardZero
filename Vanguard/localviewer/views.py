from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

def index(request):
    DayToday = datetime.today()
    DayTomorrow = DayToday+timedelta(1)
    DayTomorrower = DayToday+timedelta(2)
    
    return render(request, 'index.html', {"todayname":DayToday.strftime("%A"), "tomorrowname":DayTomorrow.strftime("%A"), "tomorrowername":DayTomorrower.strftime("%A")})