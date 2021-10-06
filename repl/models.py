from django.db import models


class Worker(models.Model):
    fio = models.CharField(max_length=255)
