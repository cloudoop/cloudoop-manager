from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',)

def tables(request):
    return render(request,'tables.html',)

def blank(request):
    return render(request,'blank.html',)

def forms(request):
    return render(request,'forms.html',)

def flot(request):
    return render(request,'flot.html',)

def morris(request):
    return render(request,'morris.html',)

def login(request):
    return render(request,'login.html',)

def buttons(request):
    return render(request,'buttons.html',)

def panels(request):
    return render(request,'panels-wells.html',)

def typography(request):
    return render(request,'typography.html',)

def notifications(request):
    return render(request,'notifications.html',)

def grid(request):
    return render(request,'grid.html',)
