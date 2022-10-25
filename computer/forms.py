from computer.models import Client, Interface
from django.forms import ModelForm

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class InterfaceForm(ModelForm):
    class Meta:
        model = Interface
        fields = '__all__'
    
