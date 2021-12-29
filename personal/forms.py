from django import forms

class ContactForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length=50, widget=forms.TextInput(attrs={'class':'contact__input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'contact__input'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class':'contact__input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'contact__input', 'cols':'0', 'rows':'7'}))