from django import forms
from django.contrib.auth.models import User
from five_app.models import Userprofil

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields =('username','email','password')

class UserProfilInfo(forms.ModelForm):
    class Meta():
        model = Userprofil
        fields = ('profelio','profil_pic')
