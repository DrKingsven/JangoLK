from asyncio import tasks

from django.contrib.sites import requests
from django.core.serializers import serialize
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views import View
from .models import Task
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class TaskView(View):

    def post(self, request):

        post_body = json.loads(request.body)

        id = post_body.get('id')
        refUsers = post_body.get('refUsers')
        tasks = post_body.get('tasks')

        data = {
            'id': id,
            'refUsers': refUsers,
            'tasks': tasks,

        }

        task_obj = Task.objects.create(**data)
        data = {
            'message': f'New task object has been created with id {task_obj}'
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        tasks = Task.objects.all()

        tasks_serialized_data = serialize('python', tasks)

        data = {
            'tasks': tasks_serialized_data,
        }
        return JsonResponse(data)
