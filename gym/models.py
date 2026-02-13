from django.db import models


ESPECIALIDAD_INSTRUCTOR = [
    ('yoga', 'Yoga'),
    ('cross fit' , 'Cross Fit'),
    ('aeróbic' , 'Aeróbic'),
    ('hiit' , 'HIIT'),
    ('pilates' , 'Pilates')
]

ESTADO_CLASE = [
    ('programada' , 'Programada'),
    ('finalizada' , 'Finalizada'),
    ('cancelada' , 'Cancelada')
]
# Create your models here.
class InstructorModel (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=20, choices=ESPECIALIDAD_INSTRUCTOR)
    activo = models.BooleanField(default=True)

class ClaseModel (models.Model):
    nombre = models.CharField(max_length=20)
    instructor = models.ForeignKey(InstructorModel, on_delete=models.CASCADE, related_name='instructor')
    fecha_hora = models.DateTimeField()
    cupo = models.IntegerField(default=20)
    estado = models.CharField(max_length=20, choices=ESTADO_CLASE)

class ReservaModel (models.Model):
    nombre_alumno = models.CharField(max_length=20)
    email_alumno = models.EmailField()
    clase = models.ForeignKey(ClaseModel, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    codigo_reserva = models.CharField(max_length=10)