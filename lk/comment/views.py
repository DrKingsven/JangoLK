from django.core.serializers import serialize
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views import View
from .models import Сomment
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class СommentView(View):
    def post(self, request):
        post_body = json.loads(request.body)  # don't forget to import jsontitle = post_body.get('title')
        data = post_body.get('data')


        data = {
            'data': data,

        }

        comment_obj = Сomment.objects.create(**data)
        data = {
            'message': f'Новый обьект записан в базу под uuid {comment_obj.id}'
        }

        return JsonResponse(data, status=201)

    # class TaskViews(View):
    def get(self, request):
        comment = Сomment.objects.all()

        comment_serialized_data = serialize('python', comment)

        data = {
            'comment': comment_serialized_data,
        }
        return JsonResponse(data)
