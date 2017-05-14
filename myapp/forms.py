from django import forms
from myapp.models import Login


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class blockscreenForm(forms.Form):
    class Meta:
        model = Login

class Check(forms.Form):
    WineID = forms.CharField(max_length=100)

class CreateWine(forms.Form):
    WineID = forms.CharField(max_length=100)
    OwnerInfo = forms.CharField(max_length=100)

class transferWine(forms.Form):
    WineID = forms.CharField(max_length=100)
    OwnerInfo = forms.CharField(max_length=100)
