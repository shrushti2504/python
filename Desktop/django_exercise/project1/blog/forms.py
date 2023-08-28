from django import forms

class loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)