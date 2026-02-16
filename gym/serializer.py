from rest_framework import serializers
from .models import InstructorModel, ClaseModel, ReservaModel
from django.utils import timezone

class InstructorSerialiser (serializers.ModelSerializer):
    class Meta:
        model = InstructorModel
        fields = ['nombre', 'apellido', 'especialidad']
        
class ClaseSerializer (serializers.ModelSerializer):
    class Meta:
        model = ClaseModel
        fields = ['nombre', 'instructor', 'fecha_hora', 'estado']

    def validate_fecha_hora(self, value):
        ahora = timezone.now()

        if(value < ahora):
            raise serializers.ValidationError('La clases no pueden ser programadas en dias posteriores a la fecha actual')

        return value
        
class ReservaSerializer (serializers.ModelSerializer):
    class Meta:
        model = ReservaModel
        fields = ['nombre_alumno', 'email_alumno', 'clase']
        read_only_fields = ['fecha_reserva', 'codigo_reserva']

    def validate(self, data):
        clase = data.get('clase')
        ahora = timezone.now()

        cupos_actuales = clase.cupos.count()
        if(cupos_actuales >= 20 or cupos_actuales == 0):
            raise serializers.ValidationError('La clase no cuenta con cupos disponibles')
        
        if(clase.fecha_hora < ahora):
             raise serializers.ValidationError('La clases no pueden ser programadas en dias posteriores a la fecha actual')