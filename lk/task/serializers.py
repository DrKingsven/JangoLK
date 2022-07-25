import uuid

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("pk", "id", "refUsers", "tasks")

# to_internal_value
