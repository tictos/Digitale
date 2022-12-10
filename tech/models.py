from django.db import models

# Create your models here.

class Maquette(models.Model):
    tag = models.CharField(max_length=100)
    prix = models.PositiveIntegerField()
    description = models.TextField()
    pt_description = models.TextField()
    nb_page = models.PositiveIntegerField()
    nb_api = models.PositiveIntegerField()  
    

    def __str__(self):
        return self.tag
    