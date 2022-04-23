from django import forms



class ContactForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField(required=True)
    phone = forms.CharField()
    message = forms.CharField(required=True, widget=forms.Textarea)