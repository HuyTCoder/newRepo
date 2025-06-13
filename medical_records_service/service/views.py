from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Encounter, MedicalRecord, Attachment
from .serializers import EncounterSerializer, MedicalRecordSerializer, AttachmentSerializer

class EncounterViewSet(viewsets.ModelViewSet):
    queryset           = Encounter.objects.all()
    serializer_class   = EncounterSerializer
    permission_classes = [IsAuthenticated]
    lookup_field       = "id"

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset           = MedicalRecord.objects.all()
    serializer_class   = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]
    lookup_field       = "id"

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset           = Attachment.objects.all()
    serializer_class   = AttachmentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field       = "id"
