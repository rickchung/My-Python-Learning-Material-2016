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

# Overview

## Web Application

> "In computing, a web application or web app is a client-server software application in which the client (or user interface) runs in a web browser" --  [Wikipedia - Web application](https://en.wikipedia.org/wiki/Web_application)

對於生在現代的同學來說，應該對於網頁應用程式完全不陌生，因為我們經常在使用的 Gmail、Dropbox 或是我們課程中的 Trello 和 hackpad，都是網頁應用程式的一種呈現。但就像很多我們覺得理所當然的技術一樣，如果我們從歷史的角度來看這樣東西就會覺得非常不可思議。

間單來說，網頁應用程式就是一種能夠「透過瀏覽器的介面」進行操作的應用程式。相較於過去的應用程式得透過特定平台的 GUI 介面、文字介面來運行，網頁應用程式讓我們能夠專注在程式的邏輯本身，而介面的部分就交由網頁技術如 HTML 等，不再需要處理不同平台的介面問題。

只要透過網路就能夠將我們開發的應用程式部署到任何地方，大大的節省了過去需要為不同平台開發不同城市的成本，因此網頁應用程式也越來越受到企業的重視。

## Web Framework

所謂的 framework 通常中文譯為「框架」，意指一種「預先定義好的程式架構」，在使用框架開發程式時，我們只需要把功能填入框架之中，框架就能夠依照預先定義的流程運作。

在過去我們想要開發一套基於網頁的應用程式，我們可能需要從分析設計開始定義整個系統的架構，接著針對系統中不同的功能進行開發、測試，最後將功能與系統架構整合，這樣的開發過程非常的耗費人力物力，尤其在一家企業沒有過去的程式基礎時，要投入如此龐大的資源來開發一套自己的網路應用程式是非常困難的。

Web framework 就是一種幫助你開發 Web 程式的 framework，透過該 framework 預先定義好的程式架構，我們只需要專注在功能的開發，其他攸關程式架構、流程以及部署等等的問題都交由 Web framework 解決，大大的減少了開發一套 Web application 所需要的成本。

網頁框架有很多類型，這邊我們要介紹的是比較多用途的 Django，還有另外一個跟他很像的是 Ruby on Rails（RoR）。


## Django 簡介

## 釐清 Django, Apache, PHP 和 MySQL 之間的關係


# MVC 設計概念: Model, View and Controller

## Django 中的 MVC: MTV


# Django 起手式

## 安裝 Django

在這份教學中我們會使用 1.9.2 版本的 Django，我們同樣可以使用 pip 來安裝，請在 terminal/cmd 中鍵入以下指令：

```bash
$ pip install django==1.9.2 # 要確定你的 pip 是安裝 Python3 的 Django
```

接著 pip 就會自動幫你安奘好需要的套件。

> **工作之前請檢查一下 django 的版本**
> 
> 當你使用他人提供的軟體工具時，一定要注意版本的問題，尤其是熱門的軟體工具，通常他們更新的速度會非常快，可能你今天可以跑的程式在更新之後就完全不會動了，因此使用任何軟體工具都要注意你所習慣的版本跟目前環境中的版本是不是一致的。
> 
> 如果在未來你想拿 django 糊口的話，你一定會遇到環境中使用的 django 版本跟你學的版本不同的情況（尤其在追求穩定性的企業中，通常不會使用最新版的軟體），那時你必須去查閱不同版本間的差異在哪，才不會寫出無法使用的功能。
> 
> 但我想就學習新東西新概念來說，用新版本的軟體並不是件壞事。

## 建立 Project & App

### 設定時區以及資料庫

## Model 抽象化、物件導向的資料模型

### Querysets

### 懷念 SQL 嗎？

## Django Admin 介面

## Django URLs

## Template 網頁的骨架

### HTML 

### Django Template Language

### Javascript 要怎麼辦？（補充）

## View 動態網頁的基礎

### 連結資料庫

### 處理 POST, GET 資料

### 使用者認證機制

## 處理 CSS 檔案 (static files)


# Django 提供的其他功能

## Django 表單

## 404 Not Found


# 把你的 Django 程式部署到網路上

---

# 延伸閱讀

## WSGI

## Nginx & PostegreSQL





