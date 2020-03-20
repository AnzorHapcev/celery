from __future__ import absolute_import, unicode_literals
from time import sleep
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def sleeped(duration):
    sleep(duration)


@shared_task
def send_email_task():
    sleep(4)
    send_mail(
        'Test'
        'This is from Anzor',
        'anzor20202020@gmail.com',
        ['anzorhapcev@gmail.com','hapceva@gmail.com']
    )