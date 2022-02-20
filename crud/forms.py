from django.forms import ModelForm
from crud.models import employee
from django import forms
from django.core.validators import RegexValidator
from django.db import models


alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class empoyeeform(ModelForm):
    class Meta:
        model  = employee
        fields = [ 'name', 'email' , 'address' , 'number' ] 


'''

class empoyeeform(forms.Form):
    name   = models.CharField(max_length=50, validators=[alphanumeric])
    email  = models.EmailField()
    address= models.CharField(max_length=255, validators=[alphanumeric])
    number = models.IntegerField()
    def save(self):
        data = self.cleaned_data
        user = User(name=data['name'], email=data['email'], address=data['address'], number=data['number'])
        user.save()
'''