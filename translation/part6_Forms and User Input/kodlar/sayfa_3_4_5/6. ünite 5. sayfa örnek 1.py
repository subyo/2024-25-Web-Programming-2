from django import forms
class ContactForm(forms.Form):
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        verify_email = cleaned_data.get("verify_email")

        if email != verify_email:
            raise forms.ValidationError("Lütfen e-posta adreslerinin eşleştiğinden emin olun")