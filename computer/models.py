
from django.db import models

class Interface(models.Model):
    '''
    Interface concerant la connexion d'un ordinateur.
    '''
    name    = models.CharField(max_length=255,default=None)
    addr    = models.CharField(max_length=255,default=None)
    ip      = models.CharField(max_length=255,default=None)
    dubnet  = models.CharField(max_length=255,default=None)
    gateway = models.CharField(max_length=255,default=None)
    mac     = models.CharField(max_length=255,default=None)

    def __str__(self) -> str:
        return self.name

class Computer(models.Model):
    '''
    Ordinateur qui contient une interface réseau et des information sur l'espace de stockage.
    '''
    name    = models.CharField(max_length=255,default=None)
    total   = models.FloatField(default=None)
    free    = models.FloatField(default=None)
    used    = models.FloatField(default=None)
        
    def __str__(self) -> str:
        return '{}, {}, {}, {}'.format(self.name, self.total, self.free, self.used)

class Client(models.Model):
    '''
    Client qui contient des ordinateurs.
    '''
    name    = models.CharField(max_length=255,default=None)
    address = models.CharField(max_length=255,default=None)
    zip     = models.CharField(max_length=255,default=None)
    city    = models.CharField(max_length=255,default=None)
    phone   = models.CharField(max_length=255,default=None)
    mail    = models.CharField(max_length=255,default=None)

    def __str__(self) -> str:
        return self.name