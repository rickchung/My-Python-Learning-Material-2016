from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate, Region, Vote

# Create your views here.

def index(request):
    """ Show the index page
    """
    return HttpResponse("Hello world. This is the stats index.")

def candidate(request, candidate_id): # 這裡的參數將會從 URLConf 解析而來
    """ Show the details of candidate
    """
    return HttpResponse("You are watching the details of candidate <b>{id}</b>".format(id=candidate_id))

def region(request, region_name):
    """ Show the vote results of one region
    """
    return HttpResponse("You are watching the details of region <b>{name}</b>".format(name=region_name))
