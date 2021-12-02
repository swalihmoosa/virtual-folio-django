from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import EmailInput, TextInput, Textarea
from web.models import Contact, Subscribe


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "name" : TextInput(attrs={"placeholder" : "Enter Your Name","class" : "name"}),
            "email" : EmailInput(attrs={"placeholder" : "Enter Your Email"}),
            "subject" : TextInput(attrs={"placeholder" : "Subject", "class" : "subject"}),
            "message" : Textarea(attrs={"placeholder" : "Enter message here","rows" : 10, "cols" : 30}),
        }


class SubscribeForm(ModelForm):

    class Meta:
        model = Subscribe
        fields = "__all__"
        widgets = {
            "email" : EmailInput(attrs={"placeholder" : "Enter Email"}),
        }