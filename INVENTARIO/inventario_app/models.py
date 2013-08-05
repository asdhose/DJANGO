from django.db import models

# Create your models here.

class  Categoria(models.Model):
	idcategoria = models.IntegerField
	descripcion = models.CharField(max_length=200)

class Producto(models.Model):
	idproducto = models.IntegerField
	idcategoria = models.ForeignKey(Categoria)
	descripcion = models.CharField(max_length=200)
	stock = models.IntegerField
