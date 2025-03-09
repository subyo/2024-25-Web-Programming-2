from django import forms
class ContactForm(forms.Form):
    
    def clean_mail(self):
        email = self.cleaned_data.get('email')
        if "example.com" not in email:
            raise forms.ValidationError("Lütfen example.com e-posta adresinizi kullanın")
        return email