from django.test import TestCase
import json
import requests
from django.http import JsonResponse


def my_api_view(request):
    response = requests.get(
        "http://Kirill:79782825742@192.168.1.10/taskmanager/hs/ExchangeSUZ/clients/?user=79787507227")

    print(response.status_code)
