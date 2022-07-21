import uuid

from django.db import models


class Profiluser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    refUsers = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    clients = models.JSONField(null=True, blank=True)