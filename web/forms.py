from django import forms
from django.forms import ModelForm
from django.forms.widgets import EmailInput, TextInput
from web.models import Contact
from web.models import INTEREST


EMPTY_INTEREST = (("","Interested In..."),) + INTEREST


class ContactForm(ModelForm):

    interest = forms.ChoiceField(choices=EMPTY_INTEREST)
    
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "email" : EmailInput(attrs={"placeholder":"Email"}),
            "name" : TextInput(attrs={"placeholder":"Full Name"}),
            "number" : TextInput(attrs={"placeholder":"Phone"}),
        } 

