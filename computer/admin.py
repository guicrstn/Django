from django.contrib import admin

from computer.models import Client

class ClientAdmin(admin.ModelAdmin):
    '''
    Classe de personnalisation du formulaire et table du champ d'administration d'un client.
    '''
    pass # TODO : Afficher le nom et la date d'ajout du client

admin.site.register(Client,ClientAdmin)