# -*- coding: utf-8 -*-
# from event.models import Event


from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect
from planApp.models import Departments, Teachers,Room
from django.db import connection
from django.db.models import Q
from .forms import NameForm



def home(request):
    if request.user.is_authenticated():
        return render(request, "adminDashboard/main.html", {})
    else:
        return render(request,"welcome.html",{})

def addDepartment(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT idOfDepartment AS id, departmentName  FROM departments ''')
    results = cursor
    if request.method == 'POST':
        if request.POST.get("Department")!="":
            name2 = request.POST.get("Department")
            depart = Departments(departmentname=name2)
            depart.save()
            cursor = connection.cursor()
            cursor.execute('''SELECT idOfDepartment AS id, departmentName  FROM departments ''')
            results = cursor
            return render(request, "adminDashboard/addDepartment.html", {"results": results})
        else:
            return render(request, "adminDashboard/addDepartment.html", {"results": results})
    if request.method == 'GET':
        a =  list(request.GET)
        if len(a)>0:
            depart = Departments(idofdepartment=a[0])
            depart.delete()
            cursor = connection.cursor()
            cursor.execute('''SELECT idOfDepartment AS id, departmentName  FROM departments ''')
            results = cursor
            return render(request, "adminDashboard/addDepartment.html", {"results": results})
    return render(request, "adminDashboard/addDepartment.html", {"results": results})



def addGroup(request):
    return render(request, "adminDashboard/addGroup.html", {})

def addRoom(request):
    if request.method == 'POST':
        nameRoom = request.POST.get("nameOfRoom")
        numerRoom =request.POST.get("Number")

    #     dodanie do bazy



    if request.method == 'GET':
        a =  list(request.GET)
        if len(a)>0:
            teach = Room(idofroom=a[0])
            teach.delete()

    cursor2 = connection.cursor()
    cursor2.execute('''select * from room''')
    results = cursor2
    cursor2.close()

    return render(request, "adminDashboard/addRoom.html", {"results":results})

def addWorker(request):
    if request.method == 'POST':
        title = request.POST.get("Title")
        nameForm = request.POST.get("Name")
        surnameForm = request.POST.get("Surname")
        department = request.POST.get("Department")
        worker =  Teachers(title=title,name=nameForm,surname=surnameForm,departmentid=department)
        worker.save()
    if request.method == 'GET':
        a =  list(request.GET)
        if len(a)>0:
            teach = Teachers(idofteacher=a[0])
            teach.delete()
    cursor = connection.cursor()
    cursor.execute('select idOfTeacher,title,name,surname,departmentName,idOfDepartment from teachers, departments where teachers.departmentId=departments.idOfDepartment;')
    teachers = cursor
    cursor.close()

    cursor2 = connection.cursor()
    cursor2.execute('''SELECT idOfDepartment AS id, departmentName  FROM departments ''')
    results = cursor2
    cursor2.close()
    return render(request, "adminDashboard/addWorker.html", {"teachers":teachers,"results": results,})
