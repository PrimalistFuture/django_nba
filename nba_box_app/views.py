from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World, you are at the nba_box index, and should see all of the games played yesterday.')

def standings(request):
    return HttpResponse('This will be where overall standing are located.')

def team(request, team):
    response = 'You are looking at %s games from the past week.'
    return HttpResponse(response % team)

# def player(request, team, player):
#     return HttpResponse('You are looking at  %s of game details from the past week.' % player and team)
