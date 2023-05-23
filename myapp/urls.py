from django.urls import path,include
from . import views
urlpatterns = [
path('', views.index,name="index"),
path('services/',views.services,name="services"),
path('team/',views.team,name="team"),
path('project/',views.project,name="project"),
path('details/<int:id>/',views.details,name="details"),
]