from rest_framework.routers import DefaultRouter
from .views import EncounterViewSet, MedicalRecordViewSet, AttachmentViewSet

router = DefaultRouter()
router.register(r"encounters", EncounterViewSet, basename="encounter")
router.register(r"records",    MedicalRecordViewSet, basename="record")
router.register(r"attachments",AttachmentViewSet, basename="attachment")

urlpatterns = router.urls
