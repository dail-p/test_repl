import random
import string

from django.http import HttpResponse
from django.shortcuts import render

from repl.models import Worker


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def create_few_workers(request):
    Worker.objects.bulk_create(
        [Worker(fio=generate_random_string(10)),
         Worker(fio=generate_random_string(10)),
         Worker(fio=generate_random_string(10))]
    )
    return HttpResponse("OK. Three workers was creating")


def get_workers_from_main(request):
    names = list(Worker.objects.values_list('fio', flat=True))
    return HttpResponse(str('<br>'.join(names)))


def get_workers_from_repl(request):
    names = list(Worker.objects.using('replica').values_list('fio', flat=True))
    return HttpResponse(str('<br>'.join(names)))


def get_workers(request):
    try:
        names = list(Worker.objects.values_list('fio', flat=True))
    except:
        names = list(Worker.objects.using('replica').values_list('fio', flat=True))
    return HttpResponse(str('<br>'.join(names)))

