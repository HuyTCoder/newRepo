from django.db import models
from uuid import uuid4

class Encounter(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    patient_id  = models.UUIDField()                          # foreign ref (patient_service)
    doctor_id   = models.UUIDField(null=True, blank=True)     # foreign ref (doctor_service)
    occurred_at = models.DateTimeField()
    reason      = models.CharField(max_length=255)
    facility    = models.CharField(max_length=255)

class MedicalRecord(models.Model):
    class RecordType(models.TextChoices):
        NOTE       = "note",       "Clinical note"
        DIAGNOSIS  = "diagnosis",  "Diagnosis"
        PROCEDURE  = "procedure",  "Procedure"
        RESULT     = "result",     "Lab/Imaging result"
        IMMUNIZ    = "immuniz",    "Immunization"

    id            = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    encounter     = models.ForeignKey(Encounter, related_name="records", on_delete=models.CASCADE)
    record_type   = models.CharField(max_length=20, choices=RecordType.choices)
    description   = models.TextField()
    created_at    = models.DateTimeField(auto_now_add=True)
    author_id     = models.UUIDField()  # doctor/nurse id

class Attachment(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    record      = models.ForeignKey(MedicalRecord, related_name="attachments", on_delete=models.CASCADE)
    file_path   = models.CharField(max_length=255)
    media_type  = models.CharField(max_length=120)
    uploaded_at = models.DateTimeField(auto_now_add=True)
