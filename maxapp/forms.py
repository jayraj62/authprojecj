from dataclasses import fields
from django import forms
from .models import  usersignup,notesdata,contactdata

class userform(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'
        
class notesForm(forms.ModelForm):
    class Meta:
        model=notesdata
        fields='__all__'

class contform(forms.ModelForm):
    class Meta:
        model=contactdata
        fields='__all__'
