from django.db import models


class Profiluser(models.Model):
    data = models.TextField(max_length=1000000, blank=True)
    # title = models.CharField(null=True, max_length=100, verbose_name="Клиент")
    # counterparty_inn = models.CharField(null=True, max_length=100, verbose_name="ИНН")
    # email_address = models.CharField(null=True, max_length=100, verbose_name="Эллектронный адрес")
    # client_address = models.CharField(null=True, max_length=100, verbose_name="Адрес клиента")
    # form_clients_work = models.CharField(null=True, max_length=100, verbose_name="Форма работы клиента")
    # block = models.CharField(null=True, max_length=100, verbose_name="Блок")
    # cost_hour = models.CharField(null=True, max_length=100, verbose_name="Стоимость часа")
    # holding = models.CharField(null=True, max_length=100, verbose_name="Холдинг")
    # type_payment = models.CharField(null=True, max_length=100, verbose_name="Вид оплаты")


