from django.db import models


class Interface(models.Model):
    '''
    Class: Interface
    Description: Classe qui permet de repertorié:
    - Nom
    - Addr
    - IP
    - Masque de sous réseaux
    - Passerelle
    - Adresse mac
    '''
    name    = models.CharField(max_length=255,default=None)
    addr    = models.CharField(max_length=255,default=None)
    IP      = models.CharField(max_length=255,default=None)
    Subnet  = models.CharField(max_length=255,default=None)
    Gateway = models.CharField(max_length=255,default=None)
    Mac     = models.CharField(max_length=255,default=None)

    def __str__(self) -> str:
        return f'{self.addr}, {self.IP}, {self.Subnet}, {self.Gateway}, {self.Mac}'
    def getaddr(self):
        return self.addr
    def getip(self):
        return self.IP
    def getsubnet(self):
        return self.Subnet
    def getgateway(self):
        return self.Gateway
    def getmac(self):
        return self.Mac
    def getname(self):
        return self.name


class Computer(models.Model):
    '''
    Class: Computer
    Description: Classe qui permet de repertorié:
    - Nom
    - Espace disque total
    - Espace disque restant
    - Espace disque utilisé 
    '''
    name    = models.CharField(max_length=255,default=None)
    total   = models.FloatField(default=None)
    free    = models.FloatField(default=None)
    used    = models.FloatField(default=None)

    def __str__(self) -> str:
        return '{}, {}, {}, {}'.format(self.name, self.total, self.free, self.used)
    def totaldisk(self):
        return self.total // (2**30)
    def useddisk(self):
        return self.used // (2**30)
    def freedisk(self):
        return self.free // (2**30)
    def getname(self):
        return self.name
'''
class Plateau(models.Model):
    plateau_name = models.CharField((u'Nom du plateau technique'), max_length=200)
 
    def __unicode__(self):
            return self.plateau_name
 
class Automate(models.Model):
    automate_name = models.CharField((u'Nom de l\'automate'), max_length=200)
    automate_site = models.ManyToManyField(Plateau, db_column='automate_site', verbose_name="Plateau de l'automate")
 
    def __unicode__(self):
            return self.automate_name
  '''

        
