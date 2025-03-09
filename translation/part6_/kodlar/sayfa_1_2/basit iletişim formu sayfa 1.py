from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Adınız', max_length=100)
    email = forms.EmailField(label='E-Posta')
    message = forms.CharField(label='Mesaj', widget=forms.Textarea)
