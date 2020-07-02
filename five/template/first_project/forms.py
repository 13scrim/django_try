from django import forms
from first_app.models import Topic

class NewUser(forms.ModelForm):
    class Meta:
        model = Topic
