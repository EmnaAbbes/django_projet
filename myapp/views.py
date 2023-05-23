from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
from .models import Service,Personnel,Projet,Details,Equipe
from .forms import DemandeForm,ContactForm,UserRegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
        context={'val':"Menu Acceuil"}
        return HttpResponseRedirect('/myapp')
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
        form=DemandeForm(request.POST,request.FILES)
        demande = form.save(commit=False)
        demande.userID = request.user
        demande.save()
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
def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else :
        form = UserCreationForm()
    return render(request,'registration/registration.html',{'form' : form})