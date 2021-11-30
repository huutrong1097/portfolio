from django import forms

class ContactForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length=50)
    email = forms.EmailField()
    company = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)