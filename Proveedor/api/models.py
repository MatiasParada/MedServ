from django.db import models

# Create your models here.

class MaestroProducto(models.Model):
    idp = models.IntegerField(primary_key=True)
    nomprod = models.CharField(max_length=100)
    descprod = models.CharField(max_length=300)
    precio = models.IntegerField()
    foto_prod=models.ImageField(upload_to='fotos/',blank=True, null=True)
    
    def __str__(self):
        return f'{self.idp}'