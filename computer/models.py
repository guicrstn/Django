from django.db import models

class Interface(models.Model):
    addr = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.addr


class Computer(models.Model):
    total = models.FloatField()
    free = models.FloatField()
    used = models.FloatField()

    def __str__(self) -> str:
        return '{}, {}, {}'.format(self.total, self.free, self.used)

    def totaldisk(self):
        return self.total // (2**30)
    def useddisk(self):
        return self.used // (2**30)    
    def freedisk(self):
        return self.free // (2**30)
    