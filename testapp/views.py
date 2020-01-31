from django.shortcuts import render

# Create your views here.

def index(request):
    return JsonResponse([1,2,3])
