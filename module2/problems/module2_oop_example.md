# 物件導向程式設計 Object Oriented Programming

## 複習流程：分析、設計與實作

在 reading 中我們提到了程式設計有很多不同的開發流程，現在我們要使用的是簡化版的開發流程，只使用分析、設計跟實作這三個步驟。

### 分析

- 確立你的問題
- 找出問題中主要的癥結點以及需求
- 規劃出要滿足需求會有哪些物件，以及這些物件會怎麼樣產生互動
- 物件不一定是真實的物件，也可能是抽象的概念

### 設計

- 為分析階段的物件定義細節與操作介面
- 研究解決問題的流程，試著組織物件之間的互動來滿足需求
- 規劃系統架構，找出不同的物件之間能夠以什麼樣的方式組織
- 思考一些實作上的限制

### 實作

- 寫程式碼，同時檢視分析與設計是否有遺漏之處
- 寫一些測試，看看程式碼能不能夠正確運行
- 可能會需要回到分析階段，週而復始

這一份練習基本上不會有標準答案（或是某一個格式的的輸入輸出結果），只是希望透過這樣的步驟讓大家稍微理解到物件導向的程式開發是什麼樣子，這不是解決問題的唯一方法，大家要習慣沒有標準答案的世界 ( ´ ▽ ` )ﾉ

## Exercise 1 - 物件導向分析 Object-Oriented Analysis

### Problem Identification

首先，要確定我們的問題究竟為何，在現實中你可能會需要去訪談你的顧客，花一些時間來瞭解並釐清對方的癥結點在哪裡。

但因為我們沒有真實的顧客，所以在這裡們直接沿用 module1 的問題，但是使用物件導向的方式來處理：

>才上班沒兩個禮拜的你是一家公司的系統助理，有一天老闆叫你進入辦公室，告訴你公司在上一次的系統更新後文件系統出了差錯，所有的文件都亂了序，檔名也發生了一些錯亂，那些原本應該是 「地區_使用者_2016-01-16.txt」 的檔案全部都被改了檔名，某些檔案的日期發生了錯誤，某些檔案的地區和使用者名稱變成了數字，例如「1_2_2012-01-14.txt」，這些混亂的檔案高達數百個。老闆相信你這個剛從資管系畢業的高材生，應該能很容易的就把這個問題處理好，因此命令你在今天之內把所有的檔名都變回去原本的樣子，並按照每個號碼對應的檔案所有者以及地區名稱將其分入不同的資料夾中，他希望在明天上班時能看到我們的文件系統一如過往。

### Requirement Identification

>在實際的情況中問題分析和需求分析可能會混在一起，這邊為了說明清楚所以把他們分開來看

有了問題描述之後，你就可以進行需求的分析。

一種常見的做法是「名詞-動詞」法，從問題中找出各式名詞以及動詞，來歸納整個問題（這個做法還可以幫助你取一些方法或變數的名稱）。

你可以用條列式的方法把問題中的需求攤開來看：

- 某一些檔案會被輸入
- 檔名對應表來自某一些檔案
- 根據檔名對應表來修改檔名
- 輸出修改好檔名的檔案
- 檔案要輸出到不同的資料夾中
- 能指定輸入輸出檔案位置
- （其他需求）......

### Extracting Key Concepts and Identifying Objects

接著我們要從需求之中找出「關鍵點」，這個關鍵點可能是能夠滿足需求的「重要人物」或者「重要的概念」，如果你發現某些概念或東西對你來說不是這麼的熟悉，你可能還會需要進行一些研究。

- 檔案輸入、讀取
- 檔名對應表
- 檔案改名
- 檔案輸出
- 建立資料夾
- 操作介面
- （關鍵點）......

這時你可能會發現，這些重要的關鍵點其實就是我們的「物件」，在接下來的設計階段我們要利用這些物件來定義我們的類別架構。


> 題外話：實際上在分析的時候你為了要釐清概念，可能會需要畫一些使用案例圖（use case）之類的東西，來幫助你跟你的顧客溝通。


## Exercise 2 - 物件導向設計 Object-Oriented Design

### Constructing System Architecture and Defining Object Hierarchy

在有了第一階段的物件之後，就可以把物件「抽象化」成為類別，並找出不同的類別之間的關聯。

你可以用最舒服的姿勢來思考怎麼樣把物件化為類別、把類別建構成有組織的架構。

不過呢，通常為了讓整個專案有統一的溝通方式，我們會用 UML 等作圖工具，在這一個階段會使用的是 [class diagram](http://www.ithome.com.tw/node/62186)（這一篇文章有一點點混亂，主要希望大家看一下 UML 的各種符號代表什麼意思，如果不太理解的話我再解釋）。

[IBM 的這一篇](http://www.ibm.com/developerworks/rational/library/content/RationalEdge/sep04/bell/) 似乎比較有架構一點，給大家參考看看。

![class diagram 1](https://github.com/rickchung/2016_Python_Test/blob/master/module2/problems/m2_class_diagram_1.png)

有幾件要注意的事情：

- 第一次畫 UML 圖的時候會覺得很混亂看不懂是正常的，你可能會需要邊看符號對應表邊理解到底 class diagram 在畫什麼，但多畫幾次就會慢慢習慣 ( ´ ▽ ` )ﾉ
- 因為我們的問題其實有點小，所以圖其實不會太複雜，主要是給大家當做入門指引
- 我畫的圖可能沒有很好，抱歉 (´Д` )

### Finding Associations Between Objects

接著我們要定義不同的類別物件之間「互動的細節」，例如完成一件任務的每一個步驟、牽涉到哪一些物件。

同樣你可以使用以自己的「正確姿勢」來處理，如果你不知道該如何開始的話可以嘗試使用 UML 裡面的 sequence diagram。

（一些流程圖）......

### Object Details, Attributes and Methods

類別架構以及一些物件互動的概念完成之後，接下來就可以為每一個類別定義詳細的內容，例如類別有什麼樣的方法（methods）以及什麼屬性（fields）。

同樣的我們可以使用前面的 class diagram，為每一個類別的內部加入詳細的定義。

![class diagram 2](https://github.com/rickchung/2016_Python_Test/blob/master/module2/problems/m2_class_diagram_2.png)

## Exercise 3 - 物件導向實作 Object-Oriented Implementation

實作的階段，你就可以開始根據你分析設計出來的結果來寫程式碼了。 ~~（如果你出去應徵寫程式碼的碼農的話可能只會做到這個）~~。

### Coding with Python

首先你會需要為你的專案建立資料夾結構，方便分類不同檔案，這裡有一個範例，但你不一定要依照這個範例做：

```
Project
├── README.md   <-- 放專案說明文件
├── docs        <-- 放文件檔
├── scripts     <-- 放你的 Python scripts/modules
└── tests       <-- 放你的測試模組等
```

接著你就可以根據前面的結果，一個一個去構造你的程式啦 ( ´ ▽ ` )ﾉ

>究竟怎麼樣的專案資料夾結構適合你呢？這一個問題其實很難回答，可以選用你跟你的團隊都用得舒服的架構就好。
>
>在 [這裡](http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application) 有一個討論串是討論資料夾結構的問題

### Documentation

為了要讓文件能夠靠 `sphinx` 自動產生出來，你必須要維持良好的註解習慣，但究竟什麼才是良好的註解習慣呢？通常在一個團隊裡面你們要有統一的註解規則，這樣才能讓你們的程式碼有一致的風格。

如果你不確定到底應該要怎麼寫註解的話，這裡有一些來自 [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#Comments) 的註解風格可以讓你模仿。

針對 function 的註解風格：

> "As used in this section "function" applies to methods, function, and generators.
> A function must have a docstring, unless it meets all of the following criteria: "
> - not externally visible
- very short
- obvious
>

```python
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    pass
```

針對 class 的註解風格：

>Classes should have a doc string below the class definition describing the class. If your class has public attributes, they should be documented here in an Attributes section and follow the same formatting as a function's Args section. 

```python
class SampleClass(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
```

### Writing Test

當然你也要記得為你的程式寫適當的測試，如果你不記得要怎麼樣寫測試的話可以回去看一下 reading。


## 畫圖軟體

你可以用筆跟紙畫，也可以用軟體畫，在這個範例裡我用的是 [ProcessOn](https://www.processon.com)。


## 補充：分析與設計作圖工具（抱歉我只能先放一些連結，因為這真的太多太多了 (´Д` )）

UML 是一個被廣泛使用的作圖工具，但他不是指一個單一圖，UML 裡面包含了能夠滿足各種需求的圖案工具。

使用 UML 的好處是，他能夠給你一個統一的畫圖規範，不然在過去我們可能都是用自己的「藝術作品」來跟別人講解程式的概念，結果就是每個人畫出來的東西都不一樣，也很難做整理。

通常是依據需求選用啦 ( ´ ▽ ` )ﾉ

http://www.dotspace.idv.tw/Jyemii/umlcolumn/articles/umlwriting/UMLBasics/UMLBasics.htm

### 物件分析常用工具：Use Case (UML), Class Diagram (UML)

Use Case Diagram

- https://dotblogs.com.tw/jimmyyu/archive/2010/01/18/use-case-diagram.aspx
- https://msdn.microsoft.com/zh-tw/library/dd409427.aspx

Class Diagram

- http://www.ibm.com/developerworks/rational/library/content/RationalEdge/sep04/bell/
- https://zh.wikipedia.org/wiki/%E9%A1%9E%E5%88%A5%E5%9C%96

### 流程設計常見工具：Sequence Diagram (UML), Activity Diagram (UML)

[Sequence Diagram](https://msdn.microsoft.com/zh-tw/library/dd409377.aspx)

[Activity Diagram](http://puremonkey2010.blogspot.tw/2013/11/uml-uml.html)


