from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Service,Personnel,Projet,Details
def index(request):
    return render(request,'myapp/index.html')
def services(request):
    list = Service.objects.all()
    return render(request,'myapp/services.html',{'list':list})
def team(request):
    list = Personnel.objects.all()
   
    return render(request,'myapp/team.html',{'list':list})
def project(request):
    list = Projet.objects.all()
    return render(request,'myapp/project.html',{'list':list})
def details(request,id):
    list = get_object_or_404(Details, projetID=id)
    return render(request,'myapp/projectDetails.html',{'list':list})