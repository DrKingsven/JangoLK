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
        # title = post_body.get('title')
        # counterparty_inn = post_body.get('counterparty_inn')
        # email_address = post_body.get('email_address')
        # client_address = post_body.get('client_address')
        # form_clients_work = post_body.get('form_clients_work')
        # block = post_body.get('block')
        # cost_hour = post_body.get('cost_hour')
        # holding = post_body.get('holding')
        # type_payment = post_body.get('type_payment')

        data = {
            'data': data,
            # 'title': title,
            # 'counterparty_inn': counterparty_inn,
            # 'email_address': email_address,
            # 'client_address': client_address,
            # 'form_clients_work': form_clients_work,
            # 'block': block,
            # 'cost_hour': cost_hour,
            # 'holding': holding,
            # 'type_payment': type_payment,
        }

        comment_obj = Сomment.objects.create(**data)
        data = {
            'message': f'Новый обьект записан в базу под uuid {comment_obj.id}'
        }

        return JsonResponse(data, status=201)

    # class TaskViews(View):
    def get(self, request):
        comment_count = Сomment.objects.count()
        comment = Сomment.objects.all()

        comment_serialized_data = serialize('python', comment)

        data = {
            'comment': comment_serialized_data,
            'count': comment_count,
        }
        return JsonResponse(data)
