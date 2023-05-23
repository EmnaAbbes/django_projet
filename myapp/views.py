from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Service,Personnel,Projet,Details,Equipe
from .forms import DemandeForm,ContactForm
from django.http import HttpResponseRedirect
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
    print(list)
    return render(request,'myapp/project.html',{'list':list})
def details(request,id):
    list = get_object_or_404(Details, projetID=id)
    return render(request,'myapp/projectDetails.html',{'list':list})
def equipe(request,id):
    equipe=Equipe.objects.get(projetID=id)
    list=Personnel.objects.filter(equipeID=equipe.id)
    return render(request,'myapp/equipe.html',{'list':list,'name':equipe.projetID.libelle})
def newDemande(request):
    if request.method == "POST" :
        form = DemandeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/myapp')
    else :
        form = DemandeForm()
    return render(request,'myapp/demande.html',{'form':form})
def Contact(request):
    if request.method == "POST" :
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/myapp')
    else :
        form = ContactForm()
    return render(request,'myapp/contact.html',{'form':form})