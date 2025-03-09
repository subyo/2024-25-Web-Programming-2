from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'Ana Sayfa',
        'message': 'Django ile geliþtirilen bir web sayfasýna hoþ geldiniz!'
    }
    return render(request, 'homepage.html', context)

