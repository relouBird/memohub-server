from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home_view(request):
    """Vue pour la page d'accueil"""
    return render(request, 'index.html')