from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

# Créer une fonction pour render fortune.html
def test(request):
    return render (request, "main/test.html")

def myprofile(request):
    return render (request, "main/myprofile.html")


def test2(request):
    #je passe le context dans le template
    context={"videogames" : videogames}
    return render (request, "main/test2.html", context)

#test dictionnaire
videogames = [
    {"name": "The Legend of Zelda: Breath of the Wild", "studio": "Nintendo", "year": 2017},
    {"name": "The Legend of Zelda: Ocarina of Time", "studio": "Nintendo", "year": 1998},
    {"name": "The Witcher 3: Wild Hunt", "studio": "CD Projekt Red", "year": 2015},
    {"name": "Cyberpunk 2077", "studio": "CD Projekt Red", "year": 2020},
    {"name": "Red Dead Redemption 2", "studio": "Rockstar Games", "year": 2018},
    {"name": "Grand Theft Auto V", "studio": "Rockstar Games", "year": 2013},
    {"name": "God of War", "studio": "Santa Monica Studio", "year": 2018},
    {"name": "God of War: Ragnarok", "studio": "Santa Monica Studio", "year": 2022},
    {"name": "Horizon Zero Dawn", "studio": "Guerrilla Games", "year": 2017},
    {"name": "Horizon Forbidden West", "studio": "Guerrilla Games", "year": 2022},
]


