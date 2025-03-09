from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import ContactForm

@require_http_methods(["GET", "POST"])  # Hem GET hem de POST isteklerini kabul eder
def submit_contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Başarı sayfasına yönlendir
    else:
        form = ContactForm()
    
    return render(request, 'contact_form.html', {'form': form})


from django.shortcuts import render

def home(request):
    return render(request, "home.html")
