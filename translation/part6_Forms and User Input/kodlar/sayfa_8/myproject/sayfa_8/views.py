from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm  # Formu içe aktar

# @require_POST decorator'ı ile yalnızca POST isteklerini kabul edelim
from django.views.decorators.http import require_POST

@require_POST
def submit_contact_form(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('success_page')  # Başarıya yönlendirme
    return render(request, 'contact_form.html', {'form': form})


def index(request):
    return HttpResponse("Hoş geldiniz, Sayfa 8!")



#cd C:\Users\hamza\OneDrive\Masaüstü\sayfa_8\myproject
#python manage.py runserver