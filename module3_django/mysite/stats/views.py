from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Candidate, Region, Vote

# Create your views here.

def index(request):
    """ Show the index page
    """
    # 從資料庫中抓取 Candidate 和 Rrgion 的資料

    candidate_list = Candidate.objects.all()
    region_list = Region.objects.all()

    # 製作 response content

    response = "Candidates: {clist} <br>Regions: {rlist}".format(
        clist=', '.join([c.candidate_name for c in candidate_list]), 
        rlist=', '.join([r.region_name for r in region_list]))

    return HttpResponse(response)

def candidate(request, candidate_id): # 這裡的參數將會從 URLConf 解析而來
    """ Show the details of candidate
    """
    try:
        c = Candidate.objects.get(id=candidate_id)
    except Candidate.DoesNotExist:
        raise Http404('Candidate of id {id} does not exist.'.format(id=candidate_id))

    return HttpResponse("{name}, {gender}, {age}".format(
        name=c.candidate_name,
        gender=c.candidate_gender,
        age=c.candidate_age))

def region(request, region_name):
    """ Show the vote results of one region
    """
    try:
        r = Region.objects.get(region_name=region_name)
    except Region.DoesNotExist:
        raise Http404('Region of name {name} does not exist.'.format(name=region_name))

    return HttpResponse("Region: {name}".format(name=r.region_name))
        
