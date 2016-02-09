
# Module 2 - More Python, Object-Oriented Thinking and Teamworks

>目前公司正準備要開發一套簡單的網路程式，在你的團隊中有好多個程序猿，這個網路程式雖然簡單，但有許多功能跟很多不同的模組需要由不同的團隊完成。你的團隊被指派去做檔案處理的部份。
>
> 在開發時會遇到很多的問題，然而最大的問題就是，「我的程式要怎麼樣給其他人使用呢？」
>
> 這是一個非常大的問題，在過去我們寫程式時，往往都是自己寫自己的，一個 main 搞定，然而今天如果你要與他人合作完成程式，你該怎麼辦呢？
>
> 你：誒我的程式寫好了。
>
> 成員Ｂ：哦哦不錯啊，拿來吧，我們要開始整合了。
>
> 你：（給了隨身碟）
>
> 成員Ｂ：哎，還用隨身碟啊，我們不是有 Github 嗎
>
> 你：我不太會用嘛 ( ´ ▽ ` )ﾉ
>
> 成員Ｂ：好啦沒關係，下次得學會用啊。
>
> （插入隨身碟）
>
> 成員Ｂ：你的程式在哪裡啊？？
>
> 你：就在那裡啊。
>
> 成員Ｂ：我沒看到啊。
>
> 你：就在那裡啊（指 main）
>
> 成員Ｂ：......這怎麼用啊？？？有使用手冊嗎？
>
> 你：沒有誒，這很簡單啊，你就把它打開，然後把裡面的參數這樣改一下，那邊可以加上這個，你把這個註解弄掉就可以改功能設定，然後看妳要用在哪裡就複製貼上，就可以啦。
>
> 成員Ｂ：......你怎麼進來的啊
>
> 你：老闆說他很喜歡用資管系的同學啊 ( ´ ▽ ` )ﾉ
>
> 成員Ｂ：......你知道什麼是物件導向嗎？
>
> 你：我知道啊，不就是有一個銀行帳戶，然後可以變成很多種不同的銀行帳戶，然後他會有一些存款提款的功能，還有帳戶裡面會有錢喔，我還可以變出很多不同的帳戶呦 ( ´ ▽ ` )ﾉ
>
> 成員Ｂ：......我看我來教教你物件導向要怎麼用吧 ◡ ヽ(`Д´)ﾉ ┻━┻
>

## 1. 學這堂課要幹麻

物件導向、團隊合作

### 在這堂課你將學會

- 物件導向分析、設計以及實作的概念
- 如何透過物件導向的方式設計程式
- Python 的物件導向實現方法
- Python 的檔案輸入輸出
- Python 的例外處理（Exception）
- Python 的 module 概念與管理工具 pip
- Python Documentation
- Git 與 GitHub

## 2. 課程大綱

- Analysis, Design and Implementation
- Object Modeling and Object-Oriented Programming
- Basic Object-Oriented Programming Process
- Analysis and Design Tools
- Python Exception
- Python Module
- Python Documentation
- Python Unit Test
- Other Useful Tools: File I/O and Argument Passing


---
# 分析、設計與實作

## 什麼是分析（Analysis）

## 什麼是設計（Design）

## 什麼是實作（Implementation）

## 為什麼這很重要

## 關於開發流程


---
# 物件導向基礎概念

## 用物件的方式思考 Object-Oriented Modeling

### 類別 Class

### 封裝 Encapsulation and Data Hiding

### 繼承 Inheritance

### 多型 Polymorphism

### 物件與物件之間的連結 Massage Passing, Links and Association

## 物件導向的好處 Benefits of Object Oriented Modeling


---
# 物件導向程式設計範例 Object Oriented Programming

## 複習流程：分析、設計與實作

## 第一步 物件導向分析 Object-Oriented Analysis

### 常用工具介紹：Use Case (UML), Class Diagram (UML)

### Problem Identification

### Requirement Identification

### Extracting Key Concepts

### Identifying Objects

## 第二步 物件導向設計 Object-Oriented Design

### 常見工具介紹：Sequence Diagram (UML), Activity Diagram (UML) and Data Flow Diagram

### Constructing System Architecture

### Finding Associations Between Objects

### Defining Object Hierarchy

### Object Details, Attributes and Methods

## 第三步 物件導向實作 Object-Oriented Implementation

### Python Class

## 補充：分析與設計作圖工具 UML


---
# 不同以往的程式流程：例外 Exception


---
# 模組的概念 Module


---
# 撰寫文件 Documentation by sphinx


---
# 單元測試 Unit Test


---
# 其他滿有用的概念：檔案讀寫與參數傳遞 File I/O and Argument Passing


---
# Git & GitHub


---
# 關於團隊合作



## 上面講的只是很小的一部份

## 軟體開發流程


---
# 延伸閱讀

## 深入理解 Python Class

了解 class 的基本用法其實就足夠你完成大多數的任務了，但稍微了解一下 Python 所提供的一些額外功能，也許能夠幫助你設計出更加靈巧的 Python 程式。

以下是幾個我覺得滿重要的東西：

- Exceptions Are Classes Too
- Iterators (`for i in [1,2,3]` remember this?)
- Generator (`yield` return results one-by-one)

完整內容請看 [Python Documentation](https://docs.python.org/3.4/tutorial/classes.html#classes)

[What can you use Python generator functions for?](http://stackoverflow.com/a/102632)

[Python's Magic Methods](http://www.rafekettler.com/magicmethods.html)

這一個滿有趣的，但內容很多，以目前來說大概知道有這個東西就行，如果你想要設計一個很棒的 Python class 可以研究看看。

## Python 有私有成員（Private Member）的概念嗎？

>“Private” instance variables that cannot be accessed except from inside an object **don’t exist in Python**. However, there is a **convention** that is followed by most Python code: **a name prefixed with an underscore** (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

[From 9.6. Private Variables](https://docs.python.org/3.4/tutorial/classes.html#tut-private)

## pip 與 easy_install

>easy_install was released in 2004, as part of setuptools. It was notable at the time for installing packages from PyPI using requirement specifiers, and automatically installing dependencies.
>
>pip came later in 2008, as alternative to easy_install, although still largely built on top of setuptools components. It was notable at the time for not installing packages as Eggs or from Eggs (but rather simply as ‘flat’ packages from sdists), and introducing the idea of Requirements Files, which gave users the power to easily replicate environments.

當你不知道該用哪個的時候，就先用 pip 吧。

[Python Packaging User Guide - pip vs easy_install](http://python-packaging-user-guide.readthedocs.org/en/latest/pip_easy_install/)

[Why use pip over easy_install?](http://stackoverflow.com/a/3220572)

## Python Decorator 

**注意，這個 decorator 不是 design pattern 裡面的那個 decorator。**

網路上有各種文章解釋這個東西，我個人覺得可以簡單理解為**把 function 包裝起來的 function**，用於「裝飾」原本的 function，增加一些額外的行為。如果你對 C 的 preprocessor 有些了解的話，可以用 macro 的方式來思考 decorator 的作用。

來自*Python 3 Patterns Recipes And Idioms *的範例：

```python
class my_decorator(object):
    def __init__(self, f):
        print('inside my_decorator.__init__()')
        f()
    def __call__(self):
        print('inside my_decorator.__call__()')

@my_decorator
def a_function():
    print('inside a_function()')

print('Finished decorating a_function()')

a_function()
```

看更多請參考 [Python 3 Patterns Recipes And Idioms](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/PythonDecorators.html#what-can-you-do-with-decorators)

Decorator 可以讓你在不動到 function 內容的情況下增加 function 呼叫時的行為，甚至可以接收一些參數。

那他到底可以用來幹嘛呢？這邊有一個[討論串](http://stackoverflow.com/questions/489720/what-are-some-common-uses-for-python-decorators)，有興趣的人可以瀏覽瀏覽。

如果不想點進去的話，這邊整理了一個小 list：

- Django login guarding
- for timing
- synchronization
- type checking
- wrap with additional functionalities

## 開發流程重不重要？

在大學裡基本上很少會遇到這個問題（除非你自己組成了一個很認真的小團隊），可能會覺得寫軟體只要能夠跑、能夠達成目標就行。但在出社會以後進了公司當個程序猿時，就不能這麼隨隨便便了（這大概是常聽到出了社會以後你才會學到工作有用的技能的原因之一吧，畢竟在大學裡很少看到這樣的工作環境。）

但在業界裡寫軟體意味者一種「生產」，軟體開發時程、軟體品質、軟體測試等等都攸關軟體這個「產品」能不能夠穩定地提供客戶他們所需的服務，為了能夠掌控軟體開發的過程，我們可能就會需要有一套「軟體生產流程」來控制整個軟體開發的各個活動。

https://dotblogs.com.tw/jimmyyu/archive/2010/06/15/importance-of-development-process.aspx

## 敏捷開發流程

不知道為什麼近年來常常聽到這個詞，放個連結給大家參考一下。

http://wiki.mbalib.com/zh-tw/%E6%95%8F%E6%8D%B7%E5%BC%80%E5%8F%91

## 改善既有程式的設計 - 軟體重構 Refactoring

http://jjhou.boolan.com/jjtbooks-refactoring.htm

