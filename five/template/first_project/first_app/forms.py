from django import forms
from django.core import validators
from first_app.models import webpage,Topic,AccesRecord
from django.forms import ModelForm


class NewForm(ModelForm):
    class Meta:
         topic = forms.ModelChoiceField(Topic.objects)

         model = webpage
         fields = "__all__"

class Newform2(ModelForm):
    class Meta :
        model = AccesRecord
        fields=('date',)
