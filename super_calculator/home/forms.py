from django import forms

class PiForm(forms.Form):
    k = forms.CharField(label='Enter a positive integer', max_length=6)
