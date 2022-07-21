import uuid

from django.db import models


class Сomment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    refTasks = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    comment = models.JSONField(null=False, blank=True)
