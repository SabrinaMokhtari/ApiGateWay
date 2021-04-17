from django.db import models

class Type(models.TextChoices):
    post = 'post'
    get = 'get'
    put = 'put'
    delete = 'delete'


class RequestRecord(models.Model):
    path = models.CharField(max_length=50)
    status_code = models.IntegerField()
    type = models.CharField(max_length=100, choices=Type.choices, default="client")
