from django.db import models


class Сomment(models.Model):
    data = models.TextField(max_length=1000000, blank=True)

