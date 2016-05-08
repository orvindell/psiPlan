# from event.models import Event
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect


def home(request):
    if request.user.is_authenticated():
        return render(request, "adminDashboard/dashboard.html", {})
    else:
        return render(request,"welcome.html",{})


		#return HttpResponseRedirect('/dashboard/')
