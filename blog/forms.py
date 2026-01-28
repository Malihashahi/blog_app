from django import forms
from django.core.validators import ValidationError



class ContactUsForm(forms.Form):
  name = forms.CharField(max_length=10, label='your name plasce')
  text = forms.CharField(max_length=10 , label='your massage')


  def clean(self):
    name = self.cleaned_data.get('name')
    text = self.cleaned_data.get('text')
    if name == text :
        raise ValidationError('invalide text')