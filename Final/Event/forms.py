from django.forms import ModelForm
from .models import *
from django import forms


class EventForm(ModelForm):
    class Meta:
        model=EventModel
        fields=['EventName','EventDate','Budget','Description','NoOfParticipants','Outcomes']


class EditSearchForm(ModelForm):
    class Meta:
        model=EditSearchModel
        fields=['EventName','EventDate']



class EmailForm(forms.ModelForm):
    email = forms.EmailField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control",'id': "clientemail"}))
    message = forms.CharField( widget=forms.Textarea(attrs={'class': "form-control"}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = Mails
        fields = ('email','subject','message','document',)
        