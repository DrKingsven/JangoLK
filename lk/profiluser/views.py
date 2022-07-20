from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views import View
from .models import Profiluser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class ProfiluserView(View):
    def post(self, request):

        post_body = json.loads(request.body)  # don't forget to import jsontitle = post_body.get('title')
        data = post_body.get('data')


        data = {
            'data': data,

        }

        profiluser_obj = Profiluser.objects.create(**data)
        data = {
            'message': f'Новый обьект записан в базу под uuid {profiluser_obj.id}'
        }

        return JsonResponse(data, status=201)
    # class TaskViews(View):
