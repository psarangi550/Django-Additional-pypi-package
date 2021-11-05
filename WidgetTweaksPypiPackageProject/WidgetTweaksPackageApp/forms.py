from django import forms
#importing the forms from django module

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    sender = forms.EmailField()
    comment=forms.CharField(widget=forms.Textarea)
