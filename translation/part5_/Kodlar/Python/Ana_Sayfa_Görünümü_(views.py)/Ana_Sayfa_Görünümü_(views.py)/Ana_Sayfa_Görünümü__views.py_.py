from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'Ana Sayfa',
        'message': 'Django ile geli�tirilen bir web sayfas�na ho� geldiniz!'
    }
    return render(request, 'homepage.html', context)

