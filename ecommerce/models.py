from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo_usuario = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo_barra = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE)  # Añadir este campo

    def __str__(self):
        return self.descripcion

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class FormaPago(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Meta:
    app_label = 'ecommerce'  # Asegúrate de agregar esto
