from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    
    return render(request, 'page/home.html')
