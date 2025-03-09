from django.shortcuts import render, redirect
from . forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            # E-posta göndermek veya bir veri tabanına kaydetmek gibi geçerli form verisini işler

            return redirect('success_url')
        
            # İşledikten sonra yeni bir URL'ye yönlendirir

        else:
            form = ContactForm()

            # Boş bir formu ekrana gösterir

        return render(request, 'contact.html', {'form': form})