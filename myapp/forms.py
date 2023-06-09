from django.forms import ModelForm
from .models import Demande,Contact,Commentaire
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class DemandeForm(ModelForm):
    class Meta :
        model = Demande
        fields = ["description"]
class ContactForm(ModelForm):
    class Meta :
        model = Contact
        fields = "__all__"
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
class CommentaireForm(ModelForm):
    class Meta :
        model = Commentaire
        fields = ["message"]