from django.db import models

# Create your models here.



class receive(models.Model):
    thefile = models.FileField(upload_to="")