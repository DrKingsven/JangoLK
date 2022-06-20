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
        post_body = json.loads(request.body)  # don't forget to import jsontitle = post_body.get('title')
        data = post_body.get('data')
        #
        # title = post_body.get('title')
        # date = post_body.get('date')
        # status = post_body.get('status')
        # counterparty_inn = post_body.get('counterparty_inn')
        # counterparty = post_body.get('counterparty')
        # formulation_task = post_body.get('formulation_task')
        # get_started = post_body.get('get_started')
        # due_date = post_body.get('due_date')
        # executor = post_body.get('executor')
        # cost_of_work = post_body.get('cost_of_work')

        data = {
            'data': data,
        #
        #     'title': title,
        #     'date': date,
        #     'status': status,
        #     'counterparty_inn': counterparty_inn,
        #     'counterparty': counterparty,
        #     'formulation_task': formulation_task,
        #     'get_started': get_started,
        #     'due_date': due_date,
        #     'executor': executor,
        #     'cost_of_work': cost_of_work,
        }

        task_obj = Task.objects.create(**data)
        data = {
            'message': f'New task object has been created with id {task_obj.id}'
        }
        return JsonResponse(data, status=201)

    def get(self, request):
      tasks_count = Task.objects.count()
      tasks = Task.objects.all()

      tasks_serialized_data = serialize('python', tasks)

      data = {
          'tasks': tasks_serialized_data,
          'count': tasks_count,
      }
      return JsonResponse(data)
    # class TaskViews(View):
