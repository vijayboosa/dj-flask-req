from django.shortcuts import render
from django.http import JsonResponse
import requests

url = 'https://google.com'

def home(request):
    response = requests.get(url)
    jsonData = {'status_code': response.status_code, 'url': url}
    return JsonResponse(jsonData)