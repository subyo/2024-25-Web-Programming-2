from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Burada formdan gelen verileri işleyebilirsin (örneğin, e-posta gönderme)
            return render(request, "success.html", {"form": form})
    else:
        form = ContactForm()
    
    return render(request, "contact.html", {"form": form})

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hoşgeldiniz!")

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hoş geldiniz!")
