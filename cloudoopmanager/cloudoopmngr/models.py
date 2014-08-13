from django.db import models

# Create your models here.

class Rack (models.Model):
    name = models.CharField(max_length=60, unique=True)
    def __unicode__(self):
        return self.name

class Host (models.Model):
    hostname = models.CharField(max_length=60, unique=True)
    mem = models.IntegerField()
    os = models.CharField(max_length=20)
    ip = models.GenericIPAddressField(protocol='IPv4')
    rack = models.ForeignKey(Rack)
    def __unicode__(self):
        return self.hostname
    
class HD (models.Model):
    AVAILABLE='AV'
    OCCUPIED='OC'
    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (OCCUPIED, 'Occupied'),
    )
    size = models.IntegerField("Size (TB)")
    path = models.CharField(max_length=60)
    host = models.ForeignKey(Host)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=AVAILABLE)    
    def __unicode__(self):
        return self.host.hostname + ':' + self.path
    
class DataNode (models.Model):
    hostname = models.CharField(max_length=60)
    host = models.ForeignKey(Host)
    hds = models.ManyToManyField(HD,limit_choices_to={'status': HD.AVAILABLE})
    def __unicode__(self):
        return self.hostname + '@'+self.host.hostname
    