from django.test import TestCase
import json
import requests
from django.http import JsonResponse

def my_api_view(request):
    data = {
        'name': request.user.username,  # username of current logged-in user, otherwise Anonymous
        'url': 'https://www.pyscoop.com/',
        'skills': ['Python', 'Django'],
    }
    return JsonResponse(data)

# data = {"Пользователь": "kirill", "Пароль": 79782825742
# }

response = requests.get("http://Kirill:79782825742@192.168.1.10/taskmanager/hs/ExchangeSUZ/clients/?user=79787507227")
# response = requests.get("http://Kirill:79782825742@192.168.1.10/taskmanager/hs/ExchangeSUZ/dokuments/?user=79787507227")

# r = requests.get("http://Kirill:79782825742@192.168.1.10/taskmanager/hs/ExchangeSUZ/dokuments/?user=79787507227")

# r = requests.get("https://egorovegor.ru/wp-json/")


# description = data["description"]
# url = data["url"]
# timezone = data["timezone_string"]
#
# print(f"Информация о сайте: {url}")
# print(f"Название: {name}")
# print(f"Описание: {description}")
# print(f"Часовой пояс: {timezone}")
# print(f"Часовой пояс: {timezone}")


print(response)
# print(response.text, "text")


# http://Kirill:79782825742@192.168.1.10/taskmanager/hs/ExchangeSUZ/Password/?pass=79787507227
# print(dir(response))
