from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Service(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.type


class Projet(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    acheve = models.CharField(max_length=1, choices=(('o', 'Oui'), ('n', 'Non')))
    image=models.ImageField(default='default_image.jpg',upload_to='projet/')
    userID = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.libelle

class Details(models.Model):
    fichier = models.FileField(upload_to='details/')
    serviceID = models.ForeignKey(Service, on_delete=models.CASCADE)
    projetID = models.ForeignKey(Projet, on_delete=models.CASCADE)
    def __str__(self):
        return self.fichier.name

class Equipe(models.Model):
    projetID=models.OneToOneField(Projet, on_delete=models.CASCADE)

class Personnel(models.Model):
    nom = models.CharField(max_length=100)
    fichier_CV = models.FileField(upload_to='personnel/cv/')
    fichier_photo = models.ImageField(upload_to='personnel/photos/')
    lien_linkedIn = models.URLField(blank=True)
    equipeID=models.ForeignKey(Equipe, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Demande(models.Model):
    description=models.TextField()
    userID=models.ForeignKey(User, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.description

class Contact(models.Model):
    nom=models.CharField(max_length=100)
    Phone=models.CharField(max_length=20)
    email=models.EmailField()
    description=models.TextField()
    def __str__(self):
        return f"Contact: {self.nom} - Email: {self.email}"

class Commentaire(models.Model):
    message=models.TextField()
    time=datetime.now()
    userID=models.ForeignKey(User, on_delete=models.CASCADE, default='')
    projetID=models.ForeignKey(Projet, on_delete=models.CASCADE)
    def __str__(self):
        return self.message