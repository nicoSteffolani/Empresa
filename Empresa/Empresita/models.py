from django.db import models

# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length=30)
    numero = models.CharField(max_length=30)
    comuna = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)

    def __str__(self):
        return self.ciudad

class Proveedor(models.Model):
    telefono = models.IntegerField(null = True)
    nombre = models.CharField(max_length=30)
    web = models.CharField(max_length=30)
    direc = models.ForeignKey(Direccion, default = None, on_delete=models.CASCADE)
    rut = models.IntegerField(null = False, unique=True)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField(null = True)
    stock = models.IntegerField(null = True)
    categori = models.ForeignKey(Categoria, default = None, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, default = None, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    produc = models.ForeignKey(Producto, default = None, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null = True)
    fecha = models.DateField()
    monto_final = models.IntegerField(null = True)
    descuento = models.IntegerField(null = True)

    def __str__(self):
        return self.produc, self.cantidad


class Cliente(models.Model):
    rut = models.IntegerField(null = False, unique=True)
    direc = models.ForeignKey(Direccion, default = None, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, default = None, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

