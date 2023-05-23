from django.forms import ModelForm
from .models import Demande,Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm
class DemandeForm(ModelForm):
    class Meta :
        model = Demande
        fields = ["description"]
class ContactForm(ModelForm):
    class Meta :
        model = Contact
        fields = "__all__"