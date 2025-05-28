from django.shortcuts import render
from django.http import HttpResponse
from .models import Heroes
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404

# Create your views here.

def index(request):
    latest_heroes_list = Heroes.objects.order_by("-age")[:]
    context = {"latest_heroes_list": latest_heroes_list}
    return render(request, "polls/index.html", context)

def detail(request, heroes_id):
    heroes = get_object_or_404(Heroes, pk=heroes_id)
    return render(request, "polls/detail.html", {"heroes": heroes})

def results(request, heroes_id):
    response = "You're looking at the results of Hero %s."
    return HttpResponse(response % heroes_id)

def vote(request, heroes_id):
    return HttpResponse("You're voting on Heroes %s." % heroes_id)