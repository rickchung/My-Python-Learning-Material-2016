# 2016 Python Tutorial Material Draft

# Module 1 - Python Basics

>才上班沒兩個禮拜的你是一家公司的系統助理，有一天老闆叫你進入辦公室，告訴你公司在上一次的系統更新後文件系統出了差錯，所有的文件都亂了序，檔名也發生了一些錯亂，那些原本應該是 「地區_使用者_2016-01-16.txt」 的檔案全部都被改了檔名，日期向前移了 4 年又 2 天，原有的地區以及擁有者名稱也變成了數字，例如「1_2_2012-01-14.txt」，這些混亂的檔案高達數百個。老闆相信你這個剛從資管系畢業的高材生，應該能很容易的就把這個問題處理好，因此命令你在今天之內把所有的檔名都變回去原本的樣子，並按照每個號碼對應的檔案所有者以及地區名稱將其分入「北區」、「中區」、「南區」以及「其他地區」的資料夾中，他希望在明天上班時能看到我們的文件系統一如過往。
>
>你該怎麼辦？

- Environment preparation 
- Sublime Text, Virtual Box, or Windows installation instruction
- Basic Python syntax
- Basic I/O
- Data types and data structures
- Variable and operators
- Flow control
- Function
- Exercise: Renaming hundreds of files with Python

# Module 2 - More Python And Teamworks

>目前公司正準備要開發一套簡單的網路程式，在你的團隊中有好多個程序猿，這個網路程式雖然簡單，但有許多功能跟很多不同的模組需要由不同的團隊完成。你的團隊被指派去做檔案處理的部份。
>
>在開發時會遇到很多的問題，然而最大的問題就是，「我的程式要怎麼樣給其他人使用呢？」
>
>這是一個非常大的問題，在過去我們寫程式時，往往都是自己寫自己的，一個 main 搞定，然而今天如果你要與他人合作完成程式，你該怎麼辦呢？
>
>你：誒我的程式寫好了。
>
>成員Ｂ：哦哦不錯啊，拿來吧，我們要開始整合了。
>
>你：（給了隨身碟）
>
>成員Ｂ：哎，還用隨身碟啊，我們不是有 Github 嗎
>
>你：我不太會用嘛 ( ´ ▽ ` )ﾉ
>
>成員Ｂ：好啦沒關係，下次得學會用啊。
>
>（插入隨身碟）
>
>成員Ｂ：你的程式在哪裡啊？？
>
>你：就在那裡啊。
>
>成員Ｂ：我沒看到啊。
>
>你：就在那裡啊（指 main）
>
>成員Ｂ：......這怎麼用啊？？？有使用手冊嗎？
>
>你：沒有誒，這很簡單啊，你就把它打開，然後把裡面的參數這樣改一下，那邊可以加上這個，你把這個註解弄掉就可以改功能設定，然後看妳要用在哪裡就複製貼上，就可以啦。
>
>成員Ｂ：......你怎麼進來的啊
>
>你：老闆說他很喜歡用資管系的同學啊 ( ´ ▽ ` )ﾉ
>
>成員Ｂ：......你知道什麼是物件導向嗎？
>
>你：我知道啊，不就是有一個銀行帳戶，然後可以變成很多種不同的銀行帳戶，然後他會有一些存款提款的功能，還有帳戶裡面會有錢喔，我還可以變出很多不同的帳戶呦 ( ´ ▽ ` )ﾉ
>
>成員Ｂ：......我看我來教教你物件導向要怎麼用吧 ◡ ヽ(`Д´)ﾉ ┻━┻ 

- Class and OOP
- File I/O
- Exception
- Module and PIP
- This is not Python -- GitHub
- Exercise: How to write program with other team members? Concept and instructions

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

- Overview
- Relation between Django, Apache, PHP and MySQL 
- Framework, MVC and web application
- Template, display information on the Web Page.
- View, dynamic Web content and application logic
- Model, abstract database, ORM and a convenient way to access your data
- Exercise: A simple Web application by Django

# Module 4 - Python Scrapy: Web Crawler and Data Processing

>（時間回到兩個月前，總統大選兩天後）
>
>老闆：誒，這次總統大選你怎麼看？
>
>你：就看電視啊。
>
>老闆：......我說你對這個局勢怎麼看？
>
>你：......我也不知道呢 ˊ_>ˋ
>
>老闆：哎，我們公司的產品受到政治影響很大呢，這次大選後很多地方的民意傾向都改變啦，我們得好好規劃一下未來我們的產品要怎麼賣，要賣到哪裡去。
>
>你：是的呢～
>
>老闆：哎，我想要瞭解一下全臺灣各個地區的投票結果是如何，然後做個分析。
>
>你：是的呢。
>
>老闆：現在請工讀生做這個要做多久啊？
>
>你：Hmmmmm 從網站找到資料，然後六都加起來好像有 150 多個區，市級有 10 多個區，然後還有 13 個縣，每縣有好幾個鄉鎮市，下面還有里，應該派十個工讀生每天做八個小時，一個禮拜可以做完吧 ˊ_>ˋ
>
>老闆：哦哦，好像還行啊。
>
>你：是啊是啊
>
>老闆：聽說你是資管系出來的吧，誒你去幫我搞定，一個禮拜後要。
>
>你：一個禮拜？老闆那是十個工讀生每天八個小時做一個禮拜啊。
>
>老闆：哎那不就是你一個月的薪水嗎？你資管系的，這個很簡單啦，交給你啦。
>
>你：ᶘ ᵒᴥᵒᶅ......

- Overview
- Web spider: Concept
- XMLparser
- Data cleaning and regular expression
- Dealing with Javascript: Using NodeJS
- Recursive parsing
- Exercise: Web crawler with Scrapy

# Module 5 - Python And Data Analysis: IPython, NumPy, SciPy and Data Visualisation

>老闆：上次你給我做的那個網站還不錯啊
>
>你：還可以啦 ( ´ ▽ ` )
>
>老闆：話說我還想要分析一下那個資料啊，看看現在的趨勢，我想知道哪些地方發生了變化。
>
>你：嗯嗯，我記得公司有統計人員，我會請他們看看
>
>老闆：哎不用麻煩啦，你上次一個禮拜就搞定十個工讀生每天八個小時做一個禮拜才做完的事，請他們做還要給加班費，我記得資管系不是也有學統計嗎？還會寫程式呢，你一個人做我只要給你一個人加班費，好划算的呢。
>
>你：......恩，不過，痾，這個...
>
>老闆：好啦交給你啦，下禮拜開會帶來啊。
>
>你：......好喔

- Overview
- Python
- Regular expression
- Data Visualisation
- NumPy and SciPy
- Exercise: Data processing, cleaning, visualising with Python

# Optional - Web Communication With JSON

- Why this? Web architecture overview
- RESTful concept
- JSON concept
- What is AJAX in our common sense?
- Exercise: Django with AJAX, Django with Android

# Optional - Python-based Simple Recommender System

- Overview
- What is recommender system?
- Exercise: Building simple recommender system

# Optional - Python And System Management: Glue Language?

- Overview
- Shell language
- System management 
- Glue language?
- Exercise: Data processing by combining small programs