# from asyncio import tasks
#
from django.contrib.sites import requests
# from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render
# import json
# from django.http import JsonResponse
# from django.views import View

# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class TaskView(View):
#
#     def post(self, request):
#
#         post_body = json.loads(request.body)
#
#         id = post_body.get('id')
#         refUsers = post_body.get('refUsers')
#         tasks = post_body.get('tasks')
#
#         data = {
#             'id': id,
#             'refUsers': refUsers,
#             'tasks': tasks,
#
#         }
#
#         task_obj = Task.objects.create(**data)
#         data = {
#             'message': f'New task object has been created with id {task_obj}'
#         }
#         return JsonResponse(data, status=201)
#
#     def get(self, request):
#         tasks = Task.objects.all()
#
#         tasks_serialized_data = serialize('python', tasks)
#
#         data = {
#             'tasks': tasks_serialized_data,
#         }
#         return JsonResponse(data)
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer

from .models import Task


class TaskAPIList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPICreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # class TaskAPIView(APIView):
    #     def get(self, request):
    #         t = Task.objects.all()
    #         return Response({'posts': TaskSerializer(t, many=True).data})
    #
    # def post(self, request):
    #     serializer = TaskSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'post': serializer.data})
    #
    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Метод добавить не валиден"})
    #
    #     try:
    #         instance = Task.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Обьект не найден"})
    #     serializer = TaskSerializer(data=request.data, instance=instance)
    #     # serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"post": serializer.data})
