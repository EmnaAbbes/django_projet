from django.urls import path,include
from . import views
urlpatterns = [
path('', views.index,name="index"),
path('services/',views.services,name="services"),
path('team/',views.team,name="team"),
path('project/',views.project,name="project"),
path('details/<int:id>/',views.details,name="details"),
path('equipe/<int:id>/',views.equipe,name="equipe"),
path('demande/',views.newDemande,name="demande"),
path('contact/',views.Contact,name="contact"),
path('register/',views.register,name="register"),
path('home/',views.home,name="home"),
path('projectUser/',views.projectUser,name="projectUser"),
path('commentaire/delete/<int:commentaire_id>/',views.delete_commentaire,name="delete_commentaire"),
]