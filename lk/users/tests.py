from idlelib import debugger

from django.test import TestCase
import json
import requests


# data = {"Пользователь": "kirill", "Пароль": 79782825742
# }

r = requests.get("http://Kirill:@localhost/test_suz/ru/hs/ExchangeSUZ/clients/?user==55555555555")
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

print(r.request, "request")
print(r.text, "text")
print(r.status_code, "status_code")
print(r.json, "status_code")




# http://Kirill:79782825742@192.168.1.10/taskmanager/   hs/ExchangeSUZ/Password/?pass=79787507227
# print(dir(response))
