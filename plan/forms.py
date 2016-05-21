from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Nazwa', max_length=100)