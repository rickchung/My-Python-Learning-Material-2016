from django.conf.urls import url    # Django 的 URLConf class

from . import views     # 你自己的 view function

urlpatterns = [
    
    # 在 urlpatterns 這一個變數中，要放的就是 URL-view function 的對應關係，
    # Django 允許我們使用 regex (regular expression) 進行 URL 的解析，這在
    # 之後的章節會再提到

    # ex: /stats/
    url(r'^$', views.index, name='index'),

    # ex: /stats/candidate/{id}/
    url(r'^candidate/(?P<candidate_id>[0-9]+)/$', views.candidate, name='candidate'),
    # ex: /stats/region/{name}/
    url(r'^region/(?P<region_name>[a-zA-Z]+)/$', views.region, name='region'),

    url(r'^show_title/(?P<title>[a-zA-Z]+)/$', views.show_title, name='show_title'),
]