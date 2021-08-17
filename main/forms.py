from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_subject = forms.CharField(max_length=40)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)