from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

# Créer une fonction pour render fortune.html


def test(request):
    return render (request, "main/test.html")


