from django import forms

class nameForm(forms.Form):
    name = forms.CharField(label="What's your name?")