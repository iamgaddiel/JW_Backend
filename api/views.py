from django.http import JsonResponse
from django.shortcuts import render



def api_index(request):
    return JsonResponse({"data": "Working perfectly fine"})