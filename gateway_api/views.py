import time

import requests
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

RequestRecords = {}

@csrf_exempt
def gateway(request):
    start = time.time()
    print(RequestRecords)
    if request.path in RequestRecords and RequestRecords[request.path] > 3:
        return HttpResponse('service is not working!', status=400)
    if request.method == 'POST':
        if request.path == "/login":
            r = requests.post('http://127.0.0.1:8001/login', params=request.POST)
        elif request.path == "/register":
            r = requests.post('http://127.0.0.1:8001/register', params=request.POST)
    else:
        if request.path == "/login":
            r = requests.get('http://127.0.0.1:8001/login', params=request.GET)
        elif request.path == "/register":
            r = requests.get('http://127.0.0.1:8001/register', params=request.GET)
        elif request.path == "/logout":
            r = requests.get('http://127.0.0.1:8001/logout', params=request.GET)
        elif request.path == "/profile":
            r = requests.get('http://127.0.0.1:8001/profile', params=request.GET)
        elif request.path == "/update":
            r = requests.get('http://127.0.0.1:8001/update', params=request.GET)
        else:
            return HttpResponseNotFound("page not found")
    end = time.time()
    if r.status_code // 100 == 5 or end - start:
        if request.path in RequestRecords:
            RequestRecords[request.path] += 1
        else:
            RequestRecords[request.path] = 1
    if r.status_code != 200 and r.status_code != 201:
        return r.status_code
    return HttpResponse(r.text, status=r.status_code)
