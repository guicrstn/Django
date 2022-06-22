from multiprocessing.connection import Client
from django.contrib import admin
from computer.models import Computer, Interface, Client

admin.site.register(Computer)
admin.site.register(Interface)
admin.site.register(Client)