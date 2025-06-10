import logging
from django.db import models
from random import randrange, choices
from django.conf import settings
from datetime import datetime
from django.utils import timezone
from django.db import transaction
from django.core.validators import FileExtensionValidator
from datetime import datetime
import uuid


class Receptionist(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    user_id: str  # FK to Auth Service user
    name: str
    email: str
    phone: str



class Patient(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    first_name: str
    last_name: str
    dob: datetime
    gender: str
    contact_info: str       # JSON-stringified or separate columns as needed
    insurance_info: str     # JSON-stringified or separate columns
    created_at: datetime = Field(default_factory=datetime.utcnow)



class Visit(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    patient_id: str         # FK → Patient.id
    receptionist_id: str    # FK → Receptionist.id
    check_in_time: datetime = Field(default_factory=datetime.utcnow)
    visit_status: str = Field(default="waiting")  # e.g., waiting, in_progress, completed, no_show
    triage_code: str = Field(default="routine")    # e.g., routine, urgent, emergency


class Appointment(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    slot_id: str            # Unique identifier for the slot (provided by Scheduling Service)
    patient_id: str         # FK → Patient.id
    receptionist_id: str    # FK → Receptionist.id
    booked_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(default="scheduled")  # e.g., scheduled, rescheduled, cancelled, no_show



class VisitorLog(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    visit_date: datetime = Field(default_factory=datetime.utcnow)
    visitor_name: str
    visitor_contact: str
    patient_id: str = Field(default=None, nullable=True)  # FK → Patient.id or None
    purpose: str
    check_in_time: datetime = Field(default_factory=datetime.utcnow)
    check_out_time: datetime = Field(default=None, nullable=True)



    
