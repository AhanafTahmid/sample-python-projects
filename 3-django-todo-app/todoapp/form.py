from django import forms
from .models import Todo

class Tform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task','completed']