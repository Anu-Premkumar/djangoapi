from django.db import models
from django.urls import reverse

# Create your models here.
class router(models.Model):
    hostName = models.CharField(max_length=14)

    def __str__(self):
        return self.hostName

    def get_absolute_url(self):
        return reverse("manage_router:detail",kwargs={'pk':self.pk})

class properties(models.Model):
    hostName = models.ForeignKey(router,related_name='routers',on_delete=models.DO_NOTHING)
    sapId = models.CharField(max_length=18)
    loopBack = models.CharField(max_length=4,default="ipv4")
    macAddress = models.CharField(max_length=17)

    def __str__(self):
        return self.sapId

    def get_absolute_url(self):
        return reverse("manage_router:update",kwargs={'pk':self.pk})
