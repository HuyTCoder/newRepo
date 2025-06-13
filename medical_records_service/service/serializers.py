from rest_framework import serializers
from .models import Encounter, MedicalRecord, Attachment

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Attachment
        fields = "__all__"

class MedicalRecordSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)
    class Meta:
        model  = MedicalRecord
        fields = "__all__"

class EncounterSerializer(serializers.ModelSerializer):
    records = MedicalRecordSerializer(many=True, read_only=True)
    class Meta:
        model  = Encounter
        fields = "__all__"
