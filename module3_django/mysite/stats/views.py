from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """ Show the index page
    """
    return HttpResponse("Hello world. This is the stats index.")

def results(request, type, id): # 這裡的參數將會從 URLConf 解析而來
    """ Shoe the vote results of the passed candidate
    """
    response = "You are looking the results of the <b>{type} {id}</b>".format(type=type, id=id)

    return HttpResponse(response)