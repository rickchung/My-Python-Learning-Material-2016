from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader    # import template loader
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Candidate, Region, Vote

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    """ Show the index page
    """

    # 我們在這裡處理 POST 過來的資料

    error_message = None
    success_message = None
    if 'submit' in request.POST:
        title = request.POST['title']

        # 通常你會需要做一些檢查清洗使用者輸入的資料

        if len(title) == 0:
            error_message = 'You should input something.'
        else:

            # 使用 HttpResponseRedirect 可以把使用者重新導向到其它頁面
            # 通常在成功接收 POST 之後建議用重新導向的方式，避免使用者
            # 不小心重新整理網頁造成重送的問題
            
            # reverse 是用來取得 URLConf 內的 URL 的一種方式，避免 hard code

            return HttpResponseRedirect(reverse('show_title', args=(title, )))

    # 取得 GET 資料
    get_data = request.GET

    # 從資料庫中抓取 Candidate 和 Rrgion 的資料

    candidate_list = Candidate.objects.all()
    region_list = Region.objects.all()

    # 我們想要傳進 template 的資料要用一個 dictionary 包起來，
    # dict 的 key 就會是你能夠在 template 中使用的變數名稱
    
    context = {
        'candidate_list': candidate_list, 
        'region_list': region_list,
        'get_data': get_data,
        'error_message': error_message,
    }

    # 使用 shortcut 中的 render function 來處理 template

    return render(request, 'stats/index.html', context)

def show_title(request, title):
    return render(request, 'stats/show_title.html', {'title': title})

def user_login(request):
    return render(request, 'stats/login_page.html', {})

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
        
