from django.urls import path
from .views import home, submit_contact_form

urlpatterns = [
    path('', home, name='home'),
    path('submit/', submit_contact_form, name='submit_contact_form'),
]


