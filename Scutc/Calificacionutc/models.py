from django.db import models

# Create your models here.
class Estudiante(models.Model):
    cedula = models.CharField(max_length=10, unique=True, primary_key=True, help_text='ingresa la cedula del estudiante')
    nombre = models.CharField(max_length=50, help_text='ingresa el nombre del estudiante')
    apellido = models.CharField(max_length=50, help_text='ingresa el apellido del estudiante')
    edad = models.PositiveIntegerField(help_text='ingresa la edad del estudiante')
    celular = models.CharField(max_length=10, blank=False)

    class Meta:
        verbose_name = 'Estudiante : '
        verbose_name_plural = 'Estudiante'

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    cedula = models.CharField(max_length=10, unique=True, primary_key=True, help_text='ingresa la cedula del docente')
    nombre = models.CharField(max_length=50, help_text='ingresa el nombre del docente')
    apellido = models.CharField(max_length=50, help_text='ingresa el apellido del docente')

    def __str__(self):
        return self.cedula

class Calificacion (models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.RESTRICT)
    docente = models.ForeignKey(Docente, on_delete=models.RESTRICT)
    producto1 = models.FloatField()
    producto2 = models.FloatField()
    producto3 = models.FloatField()
       
    def __Float__(self):
        return self.producto1, self.producto2, self.producto3

