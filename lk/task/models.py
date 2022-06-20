from django.db import models


class Task(models.Model):
    data = models.TextField(max_length=1000000, blank=True, null=True)
    #
    # title = models.CharField(max_length=100, verbose_name="Задача")
    # date = models.CharField(max_length=100, verbose_name="Дата")
    # status = models.CharField(max_length=100, verbose_name="Статус")
    # counterparty_inn = models.CharField(max_length=100, verbose_name="Контрагент ИНН")
    # counterparty = models.CharField(max_length=100, verbose_name="Контрагент")
    # formulation_task = models.TextField(blank=True, verbose_name="Формулировка задачи")
    # get_started = models.CharField(max_length=100, verbose_name="Приступить")
    # due_date = models.CharField(max_length=100, verbose_name="Срок выполнения")
    # executor = models.CharField(max_length=100, verbose_name="Исполнитель")
    # cost_of_work = models.CharField(max_length=100, verbose_name="Стоимость работ")
