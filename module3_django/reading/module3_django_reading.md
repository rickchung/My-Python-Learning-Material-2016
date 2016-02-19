# Module 3 - Python With Django: MVC and Web Application

>在檔案風波後，二月的某一天，你被老闆叫進辦公室，他覺得每次都要使用公司電腦才能夠看到資料實在是太麻煩了，而且一個一個的文字檔不但難以觀看，也不容易找到想要的東西。
>
>於是他想到了公司裡有個很會寫網頁的資管系同學（你啊），希望你能製作一個能透過網路連結的網路程式，讓他能夠舒服的在家裡的沙發上使用瀏覽器來存取公司的檔案，提供一個漂亮的介面、完善的資料搜尋系統、方便管理的資料庫以及安全的使用者認證，期限是一個禮拜。
>
>你：不好意思老闆，是一個禮拜嗎？
>
>老闆：恩，一個禮拜呦。
> 
> ...... ( ´Д`)y━･~~

## 學這堂課要幹麻

> "django: The web framework for perfectionists with deadlines."
>
> "Django makes it easier to build better Web apps more quickly and with less code."

網路應用程式是一種透過瀏覽器就可以執行的應用程式，對於現在的大學生來說應該完全不陌生，我們經常在使用的電子郵件、網路硬盤、購物網站甚至一些遊戲等都是一種網路應用程式。

如果你已經學過了 HTML、JavaScript、PHP 以及一些資料庫的概念，基本上你已經有能力架構一個網路程式。

但這是非常不足的，只是掌握這些「最基本」的技術，當你要開發一套完整的系統時，你會花非常多的時間「重新發明新的輪子」，從系統的分析設計、不同功能的開發測試到程式的架構與部署，你都得一個一個慢慢寫慢慢改，對於一個每天都很有空的學生來說還好，但對於每天每天都要花錢的企業來說，這並不是一個好的開發方案。

所以我們要「站在巨人的肩膀上」，要學習使用「前人的輪子」來打造我們自己的應用程式，不但能加快我們的開發進度，還能夠避免很多不必要的 dirty hack，這就是 Web framework 的最大用處。

如果你希望未來以網路技術為工作目標的話，能夠學會至少一種網頁應用程式的框架，在找工作是很有利的（最近看到寫 django 的只要大學畢業薪水 4 ~ 8 萬都有）。

這堂課教的不是「基礎的網路技術」，而是以網路技術為基礎，學習一種更有效率的開發方式。

## 學完這堂課你可以...

- 瞭解網路應用程式的概念
- 使用 Django 開發一套功能完整的網路應用程式
- 將自己的網路應用程式部署到網路上
- MVC 架構概念
- Django Model
- Django Template language
- Django View
- Django 表單

## 大綱

* [Module 3 - Python With Django: MVC and Web Application](#module-3---python-with-django:-mvc-and-web-application)
  * [學這堂課要幹麻](#學這堂課要幹麻)
  * [學完這堂課你可以...](#學完這堂課你可以...)
  * [大綱](#大綱)
* [Overview](#overview)
  * [Web Application](#web-application)
  * [Web Framework](#web-framework)
  * [Django 簡介](#django-簡介)
  * [釐清 Django, Apache, PHP 和 MySQL 之間的關係](#釐清-django,-apache,-php-和-mysql-之間的關係)
* [MVC 設計概念: Model, View and Controller](#mvc-設計概念:-model,-view-and-controller)
  * [Django 中的 MVC: MTV](#django-中的-mvc:-mtv)
* [Django 起手式](#django-起手式)
  * [安裝 Django](#安裝-django)
  * [建立 Project & App](#建立-project-&-app)
    * [設定時區以及資料庫](#設定時區以及資料庫)
  * [Model 抽象化、物件導向的資料模型](#model-抽象化、物件導向的資料模型)
    * [Querysets](#querysets)
    * [懷念 SQL 嗎？](#懷念-sql-嗎？)
  * [Django Admin 介面](#django-admin-介面)
  * [Django URLs](#django-urls)
  * [Template 網頁的骨架](#template-網頁的骨架)
    * [HTML](#html)
    * [Django Template Language](#django-template-language)
    * [Javascript 要怎麼辦？（補充）](#javascript-要怎麼辦？（補充）)
  * [View 動態網頁的基礎](#view-動態網頁的基礎)
    * [連結資料庫](#連結資料庫)
    * [處理 POST, GET 資料](#處理-post,-get-資料)
    * [使用者認證機制](#使用者認證機制)
  * [處理 CSS 檔案 (static files)](#處理-css-檔案-(static-files))
* [Django 提供的其他功能](#django-提供的其他功能)
  * [Django 表單](#django-表單)
  * [404 Not Found](#404-not-found)
* [把你的 Django 程式部署到網路上](#把你的-django-程式部署到網路上)
* [延伸閱讀](#延伸閱讀)
  * [WSGI](#wsgi)
  * [Nginx & PostegreSQL](#nginx-&-postegresql)


---

<!--==============================
=            Overview            =
===============================-->
# Overview

## Web Application

> "In computing, a web application or web app is a client-server software application in which the client (or user interface) runs in a web browser" --  
[Wikipedia - Web application](https://en.wikipedia.org/wiki/Web_application)

對於生在現代的同學來說，應該對於網頁應用程式完全不陌生，因為我們經常在使用的 Gmail、Dropbox 或是我們課程中的 Trello 
和 hackpad，都是網頁應用程式的一種呈現。但就像很多我們覺得理所當然的技術一樣，如果我們從歷史的角度來看這樣東西就會覺得
非常不可思議。

間單來說，網頁應用程式就是一種能夠「透過瀏覽器的介面」進行操作的應用程式。相較於過去的應用程式得透過特定平台的 GUI 介面、文字介面來運行，網頁應用程式讓我們能夠專注在程式的邏輯本身，而介面的部分就交由網頁技術如 HTML 等，不再需要處理不同平台的介面問題。

只要透過網路就能夠將我們開發的應用程式部署到任何地方，大大的節省了過去需要為不同平台開發不同程式的成本，因此網頁應用程式
也越來越受到企業的重視。

## Web Framework

所謂的 framework 通常中文譯為「框架」，意指一種「預先定義好的程式架構」，在使用框架開發程式時，我們只需要把功能填入框
架之中，框架就能夠依照預先定義的流程運作。

在過去我們想要開發一套基於網頁的應用程式，我們可能需要從分析設計開始定義整個系統的架構，接著針對系統中不同的功能進行開
發、測試，最後將功能與系統架構整合，這樣的開發過程非常的耗費人力物力，尤其在一家企業沒有過去的程式基礎時，要投入如此龐大
的資源來開發一套自己的網路應用程式是非常困難的。

如果你曾經自己用 HTML、PHP 之類的開發過一個網站，包含一些登入登出、表單、檔案上傳、後台等等功能，你大概就能體會自己造輪子是一件多累人的事情。

Web framework 就是一種幫助你開發 Web 程式的 framework，透過該 framework 預先定義好的程式架構以及常用的功能，我們只需要專注在自己產品的開發，其他攸關程式架構、流程以及部署等等的問題都交由 Web framework 解決，大大的減少了開發一套 Web application 所需要的成本。

網頁框架有很多類型，這邊我們要介紹的是比較多用途的 Django，還有另外一個很紅也跟他很像的是 Ruby on Rails（RoR）。


## Django 簡介

Django 就是一個利用 Python 撰寫的 Web application framework。

我覺得用 Django 最大的好處在於你能夠快速地與 Python 程式進行連結，非常適合快速地開發測試。

## 釐清 Django, Apache, PHP 和 MySQL 之間的關係

到底 Django 實際上做了什麼呢？他跟 Apache、PHP 或者 MySQL 之間的關係又是什麼？

對於一些同學來說可能不是非常了解網頁伺服器或者網路運作的概念，所以在這邊我稍微解釋一下他們的關係，幫助不太懂的同學釐清
概念。
<!--====  End of Overview  ====-->


<!--=================================
=            MVC Concept            =
==================================-->
# MVC 設計概念: Model, View and Controller

## Django 中的 MVC: MTV
<!--====  End of MVC Concept  ====-->


# Django 起手式

## 安裝 Django

在這份教學中我們會使用 1.9.2 版本的 Django，我們同樣可以使用 pip 來安裝，請在 terminal/cmd 中鍵入以下指令：

```bash
$ pip install django==1.9.2 # 要確定你的 pip 是安裝 Python3 的 Django
```

接著 pip 就會自動幫你安奘好需要的套件。

> **工作之前請檢查一下 django 的版本**
> 
> 當你使用他人提供的軟體工具時，一定要注意版本的問題，尤其是熱門的軟體工具，通常他們更新的速度會非常快，可能你今天可以
跑的程式在更新之後就完全不會動了，因此使用任何軟體工具都要注意你所習慣的版本跟目前環境中的版本是不是一致的。
> 
> 如果在未來你想拿 django 糊口的話，你一定會遇到環境中使用的 django 版本跟你學的版本不同的情況（尤其在追求穩定性的企
業中，通常不會使用最新版的軟體），那時你必須去查閱不同版本間的差異在哪，才不會寫出無法使用的功能。
> 
> 但我想就學習新東西新概念來說，用新版本的軟體並不是件壞事。

## 建立 Project

首先我們要建立一個 Django 的 project，在 cmd or terminal 中打入以下指令：

```bash
django-admin startproject mysite    # mysite 可以放任何你自己的 project 名稱
```

接著你就可以在目前的目錄中找到 mysite 資料夾，內容大概長這樣：

```
mysite
├── manage.py           # 與 django 互動的操作介面
└── mysite              # 與你的 project 同名的資料夾是 project 的 package，內容是 project 的各式設定
    ├── __init__.py     # 還記得我們說 Python package 是用 __init__.py 來辨識嗎？
    ├── settings.py     # 與網站相關的各式設定檔
    ├── urls.py         # 把 URL 對應到不同功能的 mapping file，可以看成一種「網站的目錄」，在後面會講解
    └── wsgi.py         # 用來與能夠執行 WSGI 的 web server 連接
```

**整個 project 資料夾就是你的網站**，如果你過去習怪使用 WAMP/LAMP 之類的東西，可以把它當成 www 資料夾一樣的感覺，
只是在 Django 裡面一個資料夾就把網頁程式需要的功能全部包在一起。

## 設定一下時區（非必要）

在建立完 project 後，可以選擇要不要調整 Django 預設的時區，打開你的 mysite/settings.py 後修改這一行：

```python
TIME_ZONE = 'Asia/Taipei'   # 會讓 Django 系統將時間轉換為我們指定的時區
```

你也不一定要修改 Django 系統的預設時區（預設是 UTC），這樣可以保持你的 Django 專案的簡潔。

## 開發用測試伺服器

在建立完 project 後，我們可以馬上看看這一個「空的」網站到底長什麼樣子，運行以下指令：

```bash
python migrate                  # 建立 Django 預設的一些資料表，在之後會說明
python manage.py runserver      # 運行開發用伺服器
```

```
Performing system checks...

System check identified no issues (0 silenced).
February 18, 2016 - 17:24:59
Django version 1.9.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

接著在瀏覽器中輸入 `http://127.0.0.1:8000/` ，你就可以看到一個最基本的 Django web app！（可以隨時透過 
 Control-C 來結束開發伺服器）

> **Note 1**
> 
> `python manage.py runserver` 背後是一個輕量的網頁伺服器（類似 Apache 的東西），通常我們在開發 Django 程式的時候會使用這樣的測試伺服器，方便我們進行測試或觀看結果。
> 
> 需要注意的是，如果要把 Django 部署在開發環境時，**不建議使用這一個測試伺服器**，部署時應該要把 Django 跟 Apache
 或者 Nginx 等專門的網頁伺服器連接起來。

> **Note 2**
> 
> 你可以改變 server 監聽的 port：`python manage.py runserver 8080`。
>
> 如果你想要讓 development server 能夠從「外面的」IP 連進來的話，可以下 
`python manage.py runserver 0.0.0.0:8000` 來讓 server 監聽所有的 public IP。

## 建立一個 App

Django app 就像我們在 Python 裡面看到的 package 和 module 一樣，一個 Django project 是
**整個網頁程式運行的環境**，而 Django app 就像**網站中的不同功能或者子網站**，一個 Django 網頁程式可以看成是各種
不同 app 的集合體，這樣的設計方便開發者將同一個 Django app 快速地移植到不同的 Django project 中。

我們可以透過以下的指令來建立一個名叫 stats 的 app：

```bash
python manage.py startapp stats
```

接著 Django 會幫你建立一個 app 需要的基本資料夾架構，大概長得像這樣：

```bash
stats
├── __init__.py
├── admin.py
├── apps.py             
├── migrations          
│   └── __init__.py
├── models.py           
├── tests.py            
└── views.py            
```

與 Django project 相同，這一個資料夾內就包含了運行一個 Django app 所需要的所有檔案，接下來的教學幾乎都會在這一個資料夾中進行。


## Hello World!

來為我們的 stats app 撰寫第一個 View 吧，打開 stats/view.py 加入：

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. This is the stats index.")
```

在完成 view function 後，我們需要在我們的網站中開一個「進入點」連接到這一個 view，透過 URLConf 我們可以指定要透過什麼樣的網址來連結到這一個 view function。

要為我們的 stats 設定 URLConf，只需要在 stats 資料夾中新增一個名為 `urls.py` 的檔案，現在你的目錄應該會長得
像這樣：

```
stats
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
├── urls.py <------ 新增的 URLConf 設定檔
└── views.py
```

在 `stats/urls.py` 中加入以下內容：

```python
from django.conf.urls import url    # Django 的 URLConf class

from . import views     # 你自己的 view function

urlpatterns = [
    
    # 在 urlpatterns 這一個變數中，要放的就是 URL-view function 的對應關係，
    # Django 允許我們使用 regex (regular expression) 進行 URL 的解析，這在
    # 之後的章節會再提到

    url(r'^$', views.index, name='index'),
]
```

在完成 stats app 內的 URLConf 後，接下來要讓 Django 系統自己的 URLConf 連結到 app 的 URLConf，
打開 `mysite/urls.py` （注意，這是 project 資料夾內的）加入以下內容：

```python
from django.conf.urls import include, url   # 我們要多 import 一個 include
from django.contrib import admin

urlpatterns = [
    
    # Django 的官方文件建議，要連結到其他 URLConf 時一律使用 include()，
    # 第二行的 admin 是一個例外

    url(r'^stats/', include('stats.urls')),  # 這是一個 list，別忘了要加 ',' 
    url(r'^admin/', admin.site.urls),
]
```

再來啟動開發用伺服器（`python manage.py runserver`），然後用瀏覽器開啟 `127.0.0.1:8000/stats/`，你就可以看到
你的 'Hello world' 了。


## 圖例：Django 接收 HTTP request 到 response 的處理流程

方便同學釐清概念，這邊我給一個非常精簡的 HTTP request 處理流程，
讓大家能夠明白我們的網頁到底是怎麼樣透過 Django 顯示出來的。

- [Client] Send HTTP request
- [Server] HTTP server receives one request
- [Server] Pass the request to Django system
- [Django] Receives the request
- [Django] Interprete the request URL with root URLConf
- [Django] If the URL matches and points to some app's URLConf, redirect
- [Djengo-app]  Interprete the request URL with app's URLConf
- [Django-app]  URL matches, redirect to the specified view function
- [Django-app]  Dealing with the request, returning the HTTP response
- [Django] Send the response to the host server
- [Server] Send the response back to the client
- [Client] See "Hello world!"

(request/response 流程圖)

## 小結（Time to take a break）

到這裡你已經走過了 Django 網頁程式開發的基本流程，還記得前面提到的 MTV 架構嗎？到這裡你已經學會了該如何建立一個
 Django view 並將它加入 Django 的 request/response flow 中。

如果你曾經撰寫過 PHP 並使用其來修改網頁內容，這個 view 的部分其實就有點像你在網頁裡插入各式各樣的 `<?php ?>` 程式碼，
你可以在 view 裡面建構自己想要的 HTTP response，或者依據使用者的 request 來產生不同的內容。

不過這樣還不夠，在接下來的章節內我們會帶大家看如何連結資料庫以及熟悉的 HTML 網頁，來強化我們的網頁應用程式。


<!--===========================
=            Model            =
============================-->
# Model 抽象化、物件導向的資料模型

## ORM

## Migration

## Querysets and Django Shell

## 懷念 SQL 嗎？

## Django Admin 介面
<!--====  End of Model  ====-->

<!--==============================
=            Template            =
===============================-->
# Template 網頁的骨架

## HTML 

## Django Template Language

## Javascript 要怎麼辦？（補充）
<!--====  End of Template  ====-->


<!--==========================
=            View            =
===========================-->
# View 動態網頁的基礎

## 連結資料庫

## 處理 POST, GET 資料

## 使用者認證機制
<!--====  End of View  ====-->


<!--==================================
=            Static Files            =
===================================-->
# 處理 CSS 檔案 (static files)
<!--====  End of Static Files  ====-->


# Django 提供的其他功能

## Django 表單

## 404 Not Found


# 把你的 Django 程式部署到網路上

---

# 延伸閱讀

## WSGI

## Nginx & PostegreSQL

## REST and RESTful

## SOAP



