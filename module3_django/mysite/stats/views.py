from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader    # import template loader

from .models import Candidate, Region, Vote

# Create your views here.

def index(request):
    """ Show the index page
    """
    # 從資料庫中抓取 Candidate 和 Rrgion 的資料

    candidate_list = Candidate.objects.all()
    region_list = Region.objects.all()

    # 我們想要傳進 template 的資料要用一個 dictionary 包起來，
    # dict 的 key 就會是你能夠在 template 中使用的變數名稱
    
    context = {
        'candidate_list': candidate_list, 
        'region_list': region_list
    }

    # 使用 shortcut 中的 render function 來處理 template

    return render(request, 'stats/index.html', context)

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
        
