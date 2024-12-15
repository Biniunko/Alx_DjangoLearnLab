from django.db import models

# notifications/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()


class Notification(models.Model):
    recipient = models.ForeignKey(
        User, related_name="notifications", on_delete=models.CASCADE
    )
    actor = models.ForeignKey(
        User, related_name="actor_notifications", on_delete=models.CASCADE
    )
    verb = models.CharField(
        max_length=100
    )  # Describes the action, e.g., "liked", "followed"
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey("target_content_type", "target_object_id")
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.recipient.username}"

    def mark_as_read(self):
        self.read = True
        self.save()
