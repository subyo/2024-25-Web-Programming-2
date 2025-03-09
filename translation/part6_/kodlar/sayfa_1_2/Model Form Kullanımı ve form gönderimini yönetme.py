from django.db import models
from django.forms import ModelForm

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
