# Module 3 Django Exercise

這一個作業希望同學能夠練習使用 django 做一個簡單的網頁程式。

回顧一下我們的問題：

>在檔案風波後，二月的某一天，你被老闆叫進辦公室，他覺得每次都要使用公司電腦才能夠看到資料實在是太麻煩了，而且一個一個的文字檔不但難以觀看，也不容易找到想要的東西。
>
>於是他想到了公司裡有個很會寫網頁的資管系同學（你啊），希望你能製作一個能透過網路連結的網路程式，讓他能夠舒服的在家裡的沙發上使用瀏覽器來存取公司的檔案，提供一個漂亮的介面、完善的資料搜尋系統、方便管理的資料庫以及安全的使用者認證，期限是一個禮拜。
>
>你：不好意思老闆，是一個禮拜嗎？
>
>老闆：恩，一個禮拜呦。
> 
> ...... ( ´Д`)y━･~~


# Exercise 1 Creating Project and App

請創建一個 django project，並新增一個 app（名稱自取），並且嘗試 runserver。

# Exercise 2 Model

請依照題目的需求，建立「你認為應該是需要的」models （還記得前一個 module 的系統分析與設計嗎？這時候就派上用場了）。

不知道有哪些 fields 可以用嗎？請參考[這裡](https://docs.djangoproject.com/es/1.9/ref/models/fields/)。

其實如果你很懶的話也可以全部都用 CharField 啦 ˊ_>ˋ

# Exercise 3 View

請依照題目的需求，建立「你認為應該要有的」views ，並設定好 URLConf。

至少要包括以下幾個頁面（大方向）：

1. stats/accounts/ ----- 負責帳號相關事宜
    1. stats/accounts/login/  ----- 登入功能
    1. stats/accounts/logout/ ----- 登出功能
1. stats/index/    ----- 首頁，介紹一下這個網頁在幹麻
1. stats/search/   ----- 可以讓使用者依照條件搜尋（地區、候選人名稱就可）
1. stats/candidate/<candidate number>/ ----- 取出某號候選人的詳細資料及各地區得票數
1. stats/region/<region name>/  ----- 取出某個地區每個候選人的詳細得票狀況

# Exercise 4 Template

為你前面所建立的 view ，做幾個漂亮的 templates。


