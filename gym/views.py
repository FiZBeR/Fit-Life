from rest_framework import viewsets, permissions, mixins
from .serializer import ClaseSerializer, InstructorSerialiser, ReservaSerializer
from .models import ClaseModel, InstructorModel, ReservaModel
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
import secrets

# Create your views here.
class ClaseViewSet (viewsets.ModelViewSet):
    queryset = ClaseModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClaseSerializer

    def perform_create(self, serializer):
        print("DATOS VALIDADOS:", serializer.validated_data) # <--- MIRA TU TERMINAL
        serializer.save()

    @action(detail=True, methods=['patch'], url_path = 'cancelar_clase')
    def cancelar_clase(self, request, pk=None):
        clase = self.get_object()

        if clase.estado == 'cancelado':
            return Response (
                {'detail': 'La clase ya se encuentra cancelada'},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        clase.estado = 'cancelada'
        clase.save()

        serializer = self.get_serializer(clase)
        return Response(serializer.data, status.HTTP_200_OK)
                
class InstructorViewSet (viewsets.ModelViewSet):
    queryset = InstructorModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InstructorSerialiser  

class ReservaViewSet (
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    queryset = ReservaModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReservaSerializer

    def perform_create(self, serializer):
        codigo = secrets.randbelow(9000000000) + 1000000000
        serializer.save(codigo_reserva=codigo)