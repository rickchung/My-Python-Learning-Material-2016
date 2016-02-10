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

>"Just knowing an object-oriented language isn't enough to create object systems. You also have to learn to "think in objects."" 
>
>-- By Craig Larman from [here](http://www.informit.com/articles/article.aspx?p=360440#)

我不是物件導向的專家，也不是很有經驗的物件導向程序猿，以下只是我個人對於物件導向的一些看法，順便說明一下這篇文章的闡述風格，希望能給予一些初學 OO 的人一些方向，如果你是 OO 的專家，有問題我們也可以討論討論。

物件導向這東西已經發展了很多很多年了，有些大牛給予了物件導向的定義，但物件導向在實際操作的時候卻沒有一定的「正確答案」，就像沒人會跟你說只要依循著某種模式你就能夠變成某位藝術大師（從這個層面上來看，物件導向似乎又變成了一種藝術？），因此在各自解釋之下出現了很多很多的講法，有些初學者可能霧裡看花，看了很久都不明白到底什麼是物件導向。

你如果去網路上搜尋「物件導向」，跑出來的結果往往五花八門，有些人可能會跟你說「物件導向就是 XXX」之類的話，或者跟你說物件導向就是「封裝、繼承跟多型」，這些都是物件導向的某一個特色或者是風格，但我感覺不能夠以此作為整個物件導向概念的體現，以下是我認為的「物件導向」，給予大家參考：

- 物件導向是一種設計的方法，架構軟體的模式，他是你在思考如何解決問題時可以依循的一種方法，特色是使用現實世界各種物體彼此互動的概念來建構
- 所謂的「物件導向程式語言」指的是「基於物件導向概念設計出來的語言」或「能夠方便你實現物件導向設計的語言」
- 寫程式就像寫文章一樣，寫出什麼樣的東西是操之在你的思考方法，不是使用 OO 程式語言寫的東西就是 OO 程式，你也可以拿不是 OO 的語言，例如 C，寫出 OO 的程式，只要你知道你在做什麼
- 封裝、繼承、多型的確是物件導向中很重要的概念，但更重要的是這些概念在解決問題時體現出來的效果，例如程式碼重用、模組化以及方便你維護程式等等
- 有些人讚頌 OO 在管理、開發和維護上的好處，有些人討厭 OO 讓簡單的東西變得複雜，甚至降低了程式的效率
- 物件導向是內功，程式語言是你的外功

這一篇閱讀會依照這幾個概念去建構，但由於 OO 的博大精深，我只能淺淺地帶過一些很基本的東西，第一次看如果無法理解也是很正常的，你通常會需要一段時間、寫過一些程式之後才能熟悉 OO 到底應該要怎麼做。如果你過去有學過 OO，覺得跟你所學的 OO 好像相差很遠，你可以選擇跳過 OO 的部分，或者參考看看別人眼中的 OO 是什麼樣子。

在這堂課的一開始，我會用一個比較有架構的流程講述程式設計的概念（有點像是 module 1 教你怎麼寫程式的那個），並且將 OO 的概念融入其中；第二個部分則是將 OO 單獨拿出來討論，說明 OO 常見的特色以及思考方式，並且使用 Python 的語法來輔助說明；第三個部分會將前面兩個部分融合，應用一個簡單的範例，大略地帶同學看怎麼樣使用 OO 的概念去設計一個程式，其中會包含一些在系統分析設計上會使用到的圖形說明工具。

以上三個部分為物件導向設計的概念，再之後則是其他與設計有關的 Python 功能。

另外在這篇教材中會有一些跟團隊合作相關的東西，因為這堂課裡的很多概念在團隊合作時是非常重要的。

總而言之，希望大家在看完這一份教材之後，能夠對於 OO 有一點點的概念，並且記得 OO 並不是什麼 silver bullet。

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

>在資管系大三的時候會修一門必修課「系統分析與設計」，對於大三以上的同學來說應該已經非常熟悉這個概念了，你可以選擇跳過這一個章節。

如果你才大二大一或者對於怎麼樣用**物件導向+系統化**的方法去設計一支程式感到很茫然的話，就繼續看下去吧。

不過這堂不是系統分析與設計課，在這裡我們不會非常非常詳細地去看每一個步驟的細節或方法（甚至不會用所謂「正式」的定義或名詞），只是給你一個大略的概念以及怎麼樣把這個概念與實際寫程式的思考結合。另外需要注意的是我所提到的分析與設計的任務，可能會跟你在其他地方看到的有所出入，因為有很多人寫過自己對於物件導向分析設計的看法，大家在讀的時候要嘗試去體會那種精神跟理解大方向，而不要去死記硬背每一個步驟。

>如果你比較想遵循大牛的路線，想要看看大牛對於物件導向分析與設計的見解，可以看看[這本](http://www.amazon.com/Object-Oriented-Analysis-Design-Applications-Edition/dp/020189551X) *Grady Booch* 所寫的書，他是發明了 UML 圖形工具的大牛。

分析、設計與實作的概念其實是抽取自一個非常有名的軟體設計方法 System Development Life Cycle, SDLC。

我們為什麼需要在寫程式之前先進行分析與設計呢？

如果今天你只是要寫一個會講 hello world 的程式，我想你應該是不需要做這些事的，甚至連想都不用想就能寫出來。

但如果今天你要完成的程式是一個需要好幾十萬行程式碼，或者是牽涉到數十人才能夠完成的大型程式（或者系統）時，你就會非常需要一個「有秩序」的方法來管理以及架構你的程式，就像任何大型工程一般（所以有軟體工程的概念）。

舉一個例子：拆除忠孝橋引道。

## 什麼是分析（Analysis）

>- 我的目標是什麼呢？
- 有哪些需求必須被滿足？
- 過程中有哪些人或哪些東西會參與進來？
- 他們有什麼樣的行為？能夠做什麼樣的事情？
- 這些人或事物怎麼樣互動？
- ......

今天想要拆除一個已經存在多年的道路，可不能隨便找了一天，就把怪手卡車開進去然後隨便亂敲亂打。

要達成我們的**需求**，有非常多的**限制**以及牽涉到的**事物**。

- 它是一條馬路，有非常多的車輛在上面來往，交通管制怎麼辦
- 再來下方有文化古蹟，我們不能在施工過程中破壞到該建物
- 整個施工期不能夠太長，以免影響到整個交通狀況
- 文化要保存多一點，因為這很重要
- 要從哪裡開始拆起
- 配合的安全措施、工人與器具
- ......

分析最重要的目的，就是去**釐清需求**、能夠達成目的**大方向**、確定**大略的架構**以及找出你**到底需要哪些東西**。

分析有很多種方法，這裡我們當然要使用物件導向的方式來進行分析，在思考物件導向分析時，你會需要完成以下幾個任務：

- 找出過程中到底有或需要哪些物件（object）
- 透過圖像化或者容易理解的方式來組織物件
- 描述物件有什麼樣的行為
- 描述物件彼此之間怎麼樣互動或他們的關係

過程中你必須從「上帝視野」來看，用大而廣的角度來探索問題，在實際操作時你可能會需要反反覆覆地去訪查、研究、討論與確認。

當然，為了能夠系統化的處理分析的工作，你可能會需要一些工具，或著畫一些圖，常見的圖有 use case 與 class diagram。

>**這段是有感而發**
>
>當你去上系統分析與設計這堂課時，「一定要認真畫圖」並且思考「為什麼你要畫那些圖」
>
>不要覺得畫那些圖好像很愚蠢（因為在大學裡你很少有機會需要去設計一個龐大的系統，或者跟人家討論），也不要傻傻的一直畫圖。
>
>雖然沒有人說，系統分析就是應該要畫某些無聊的圖或寫下一大堆看起來很理所當然的東西，但那是「一種做法」，而且是被許多人「廣為接受的一種做法」，如果你想做一個系統分析師，那些看起來很無聊的圖，將會在未來你處在茫茫的問題大海中指引你，成為你與他人溝通的一項利器，最後幫助你達到分析的目的。


## 什麼是設計（Design）

>- 我在分析中找出的人事物，他們有什麼特性？
- 有沒有辦法把這些人事物歸類呢？
- 這些人事物有什麼需要注意的東西呢？
- 我要怎麼樣叫這些人做事？要怎麼樣使用這些物品？
- 人事物之間，詳細的互動方式以及過程是怎麼樣的呢？
- ......

設計的責任是建立系統的架構，把分析的結果，加入實作上可能需要考慮的細節，或者把分析出來的概念用接近實作的方法表現出來。

物件導向設計的細節可能包括：

- 把分析找出的概念，對應到實作的上，並定義實作的細節
- 詳細定義每一個物件內容，包括性質（attribute）和操作方法（method）
- 歸納物件，找出物件的架構（hierarchy）並構造整個系統的架構
- 定義達成目標的流程
- 定義物件之間彼此互動的細節以及限制

你可能會需要的工具：sequence diagram, data flow diagram and activity diagram。


## 什麼是實作（Implementation）

實作階段就是真正開始寫程式碼的時候，但在實作時你會受到選用的程式語言本身的限制，或發現一些分析與設計時沒有考慮到的東西。

因此你可能會需要寫一寫再回顧分析與設計的階段，週而復始。

物件導向實作可能需要考慮的事：

- 寫程式碼
- 模組化
- 抽象化
- 考慮語言本身的性質與設計的差異
- 考慮重用性
- 物件互動的方式
- 單元測試


## 其他步驟：關於測試

在學校裡寫程式你可能從來沒有想過要寫測試這回事，通常是因為你的程式不太大，或者你的程式只會用一次，撰寫測試反而耗時費力，顯得畫蛇添足。

但是，當你的程式非常大，有非常多個部分，而且每天每天可能都需要改動你的程式時，單元測試會幫助你省下很多的時間（不過開始建立單元測試的過程是很辛苦的，先苦後甘）。

在 StackOverflow 上有一篇在討論 unit test 到底有沒有用的[文章](http://stackoverflow.com/questions/67299/is-unit-testing-worth-the-effort)，裡面有一些滿有趣的回答，例如這一個：

>"**Unit testing is a lot like going to the gym.** You know it is good for you, all the arguments make sense, so you start working out. There's an initial rush, which is great, but after a few days you start to wonder if it is worth the trouble. You're taking an hour out of your day to change your clothes and run on a hamster wheel and you're not sure you're really gaining anything other than sore legs and arms." - quoted from [here](http://stackoverflow.com/a/69263)

寫測試很重要，也許你現在無法體會，但是你要對這個東西有點概念。

如果你很有
心的話也可以在你未來的專案裡面加入測試的部分，並強烈要求你的組員遵循開發流程 ˊ_>ˋ

## 為什麼這很重要 - 關於開發流程

前面我們提到了分析、設計與實作的這些步驟其實是抽取自 SDLC 這一個結構化的軟體設計方法。

但你可能會聽過其他的軟體開發流程或者開發哲學，例如瀑布式、螺旋式、敏捷式、極限編程、快速軟體開發、迭代與遞進、原型開發等等，甚至在找工作的時候有些公司會說「我們採用 XXX 開發模式」、「需要熟悉敏捷開發」之類的。

如果你發現你無法理解這些東西是什麼，不要擔心受怕，花點時間 Google 一下，你會發現你很容易能夠了解他們在幹什麼。

在軟體工程發展多年以來，有各式各樣的人、各式各樣的團隊，嘗試著各式各樣的軟體開發流程與方法，**那些名詞就是人們在實際開發軟體時，曾經嘗試過的各種模式。**

我個人認為，所有軟體的開發模式概念其實都是都是彼此互通的，只不過是把我們熟悉的計劃、分析、設計、實作、測試與維護的過程，針對某些問題進行調整、排列組合、扭曲變形後產生出來的。

因為這個世界沒有正確答案，沒有所謂的 silver bullet 能夠解決所有問題，尤其在軟體高速發展的現代，在過去適用的一些開發方式可能不適合未來新的軟體，因此人們仍然在發掘更好的方法去管理和進行軟體工程。

---

# 物件導向基礎概念

在前言中我們給了一個物件導向的解釋，大家可以用它作為你了解物件導向的開頭。

>物件導向是一種設計的方法，架構軟體的模式，他是你在思考如何解決問題時可以依循的一種方法，特色是使用現實世界各種物體彼此互動的概念來建構

## 用物件的方式思考 Object-Oriented Modeling

物件導向編程最重要的事情就是「用物件的方式思考」，怎麼樣去定義一支程式裡面的各種物件，怎麼樣去定義物件之的操作方式、性質和物件之間的連結，每個人的作法可能都不太一樣，這就像畫圖一樣，對於同樣的風景，每一個人描繪出來的作品可能天差地遠。

不過有一個東西是不變的，就是這些作品的基礎，如何闡述線條、如何調配色彩等等這些繪畫的基礎，有大牛的技巧你不一定畫得出大牛的作品，但沒有反覆練習的基礎技巧，你一定畫不出大牛的作品。

物件導向程式設計也是一樣的，雖然通往解答的路線是個人造詣，但抽絲剝繭後出來的都是同樣的物件基礎，所以你必須要了解這些共通的技巧和概念。

## 物件 Object

在物件導向裡面，最重要的東西當然是「物件」，而這個物件指的是「把一支程式內的概念，用現實世界的物件來體現」。

從上面忠孝橋引道的例子中，我們可以看到很多的物件，橋是一個物件、汽車是一個物件、北門是一個物件、機具是很多個物件，人當然也是一個一個的物件。

為了要把現實世界物件的概念轉為電腦能夠實現的概念，一些偉大大牛們就給現實世界裡那些物件一些清楚的「定義」：物件是由「狀態 state」和「行為 behavior」組成的東西。

有了定義之後，程式中的物件也能夠依循現實世界物件的模式進行定義：

- 程式裡的物件同樣也有狀態跟行為
- 狀態被稱為 fields、attributes、features 或 variables
- 行為被稱為 methods 或 functions，有時候也指操作方法

<img src="object.png" alt="物件圖">

還記得我們說過「在 Python 裡面所有東西都是物件」這件事嗎？

```python
account = Account(1, 'my name')
print(account.name)             # 狀態 field
account.deposit(1000)           # 操作方法 method
print(account)                  # 會根據 __str__ 方法印出結果
print(account.withdraw(100))    # 操作方法 method
```

## 類別 Class

在瞭解了物件是什麼之後，我們需要一個「方法」來歸納所有相同的物件，並用於定義新的物件，這就是 class 的概念。

class 可以被看成「物件的藍圖」或者「物件的設計書」，透過類別我們能夠把相同的物件用有組織的方式歸納起來，並且在需要的時候透過 class 產生新的物件（產生新物件的這個動作被稱為 instantiation）

我們用 Python code 來定義一個 class 看看，請出我們的「銀行帳戶」，這是在許多物件導向語言教學中會出現的例子：

>以下範例修改自 [openhome.cc 的 Python 教學文件](http://openhome.cc/Gossip/Python/Inheritance.html)

```python
class Account(object):
    """
    Account is a class eample.
    """
    def __init__(self, id, name):  
        # 在建立新的物件時，會先執行 __init__ 這一個區塊的程式碼，其中的參數就是建立物件時可以傳入的參數
        # 這個區塊的程式碼又被稱為建構子 constructor
        self.id = id
        self.name = name
        self.balance = 0.0

    def deposit(self, amount):
        """
        deposit some amount of money to the account

        Return:
            int: the amount of money you deposit
        """
        self.balance += amount
        return amount

    def withdraw(self, amount):
        """
        withdraw some money from the account.

        Args:
            int: amount

        Return:
            int: money you want to withdraw

        Raises:
            ValueError if there is no enough balance

        >>> account.withdraw()
        """
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            raise ValueError('No enough balance')

    def __str__(self):
        # 定義在 __str__ 裡面的回傳值，會是你直接用 print(物件) 時印出來的結果
        return ('Account[id={id}, name={name}, balance={balance}]'
        .format(id=self.id, name=self.name, balance=self.balance))

if __name__ == '__main__':
    account = Account(1, 'my name')
    print(account.name)             # 狀態 field
    account.deposit(1000)           # 操作方法 method
    print(account)                  # 會根據 __str__ 方法印出結果
    print(account.withdraw(100))    # 操作方法 method
    
```

>這邊你會看到 code 裡面有一句 `if __name__ == '__main__':` ，你可能會在很多其他地方看到這樣的寫法，這是什麼意思呢？
>
>用非常直覺的方法來理解，這個語法可以用來判斷這一個 Python script 是被直接執行（例如在 ST2 裡面 build 或 `python3 xxx.script`）還是被 `import` 進別的 script 中使用。
>
>大家還記得 module 1 problem 裡面，請大家去 `import` 一些已經寫好的函示嗎？這時候這個區塊裡面的程式碼就不會被執行，但如果你打開你 `import` 的那個 Python script，直接用 ST2 build 的話，你會看到那個區塊被執行了。
>
>我覺得大家只要知道他怎麼用就好了（通常可以拿來測試你的 module），但如果你想要更詳細的解釋，可以參考看看 [StackOverflow 上的討論串](http://stackoverflow.com/a/419185)。

## 封裝 Encapsulation and Data Hiding

在上面的範例我們示範了把銀行帳戶用一個 class 「包裝」起來，裡面包含了一些 fields 跟 methods。

我們去把一些 methods 跟 fields 綜合起來並放入一個 class 中的過程就稱為封裝（encapsulation）。

封裝類別的時候，通常我們會考慮讓某些資訊只能在物件中被取用，物件與外界溝通時則一律使用物件提供的 methods，這一個概念被稱為 data hiding，這是一種物件的設計方法，他是一個滿廣的概念，但通常會這樣做的目的是為了**讓使用者只依照你規定的方法去使用你的類別（物件）**。

例如說你現在想要啟動一台汽車，你需要做的就是插入鑰匙，然後轉動。因為設計汽車的人已經把所有啟動汽車需要的流程包裝成了一個方法（啟動汽車），你不需要自己去做啟動汽車時的各個步驟（例如自己點火、接上電源），並且限制你能夠自行操作的東西來減少危險。

如此一來使用者既不需要自行操作可能會造成危險的步驟，也能夠方便快速地使用你所建構的物件。

data hiding 還有另外一個好處是當我需要改動物件裡面某個方法的內容時，我只要維持相同的操作方法，直接改變方法的內容並不會影響到原先的使用者。

## 繼承 Inheritance

繼承是物件導向中另外一個很重要的概念，用一句話簡單來說就是「方便你透過現有的類別來建立新的類別，保有現有類別 methods 與 fields 的同時，還能夠根據你的需求去擴充或重新定義 methods 和 fields」。

通常會使用繼承的目的是為了「程式碼的重用」，你今天定義了一個「載具」的類別，並定義了一些大多數載具都共有的特性或方法，當你需要不同特性的「載具」時便可以直接繼承原先的載具，然後定義出新的類別。

我們稱「被繼承的類別」為父類別（parent/base/super class），「繼承別人的類別」為子類別（derived/child/sub class）。

以下是範例，再來講講我們偉大的「銀行帳戶」：

```python
class CheckingAccount(Account):
    """
    This is a CheckingAccount derived from Account class.
    """
    def __init__(self, id, name):
        # 呼叫 parent class 的建構子
        super(CheckingAccount, self).__init__(id, name)     
        self.overdrafitlimit = 30000

    def withdraw(self, amount):
        """
        passed amount cannot exceed the sum of balance and overdrafitlimit.

        Args:
            int: amount

        Return:
            int: amount

        """
        if amount <= self.balance + self.overdrafitlimit:
            self.balance -= amount
            return amount
        else:
            raise ValueError('You cannot withdraw so much')

    def __str__(self):
        return ('CheckingAccount[id={id}, name={name}, balance={balance}, overdrafitlimit={overdrafitlimit}]'
                .format(id=self.id, name=self.name, balance=self.balance, overdrafitlimit=self.overdrafitlimit))
```

接著我們可以用一段程式碼看看執行的結果：

```python
checkingAccount = CheckingAccount(2, 'my checking account')
print(checkingAccount.name)         # 仍然可以使用父類別的 field
checkingAccount.deposit(10000)      # 使用父類別的方法
print(checkingAccount)              # 你會發現執行的是子類別的 __str__
print(checkingAccount.withdraw(10)) # 執行的是子類別的 `.withdraw()` 方法
```

其實概念很簡單，繼承別人的類別如果有自己定義的方法就會使用自己的方法，沒有的話就會去呼叫父類別的方法。

## 多型 Polymorphism

多型是一個很有趣的設計概念，作為一個發展許久的設計方法有很多不同的用法去闡述他的優點，簡單來說，透過多型的特性我們可以「用同一個操作方法，表現出不同的結果」。

不過這個概念在 Python 上面好像很難講出是個怎麼一回事，可能是因為 Python 裡面你呼叫一個方法的時候她自然而然就會根據「是誰被呼叫」來進行「那一個物件自己的操作方法」。如果你寫過 C++ 或者是 Java 之類的語言，可能會比較有不同的體會。

我覺得多型的好處只有在你寫了一些比較大的程式，或者你來自於古老的程式語言時，才比較容易有感覺。

這是關於設計上的問題，大家可以先記得多型是什麼就好（以免別人問起），總有一天你需要設計一個程式的時候你就會想起他的 ˊ_>ˋ。

簡單舉一個例子，注意最後印出來的結果，跟 AbastractClassifier, NaiveBayesClassifier 和 SMOClassifier 之間的關係。

```python
class AbstractClassifier(object):
    def __init__(self, name):
        self.name = name
        self.model = None
    def predict(self, instance):
        # predict the instance
        pass
    def trainClassifier(self, data):
        # do something to train the classifier
        pass
    def getName(self):
        return self.name

class NaiveBayesClassifier(AbstractClassifier):
    def __init__(self):
        super(NaiveBayesClassifier, self).__init__('NaiveBayesClassifier')

class SMOClassifier(AbstractClassifier):
    def __init__(self):
        super(SMOClassifier, self).__init__('SMOClassifier')

if __name__ == '__main__':
    classifiers = [NaiveBayesClassifier(), SMOClassifier()]
    for c in classifiers:
        print(c.getName()) # 注意這一個印出來的結果
```

為了減少這篇的長度，詳細的內容可以[看這裡](http://openhome.cc/Gossip/Programmer/Ad-hoc-Polymorphism.html)，雖然我覺得這一篇有點「學術」，可能要多看幾次。

用 Java 跟 C++ 寫幾個感覺看看

```java
public class Classifier {
    protected String name;

    public Classifier(String name){
        this.name = name;
    }

    public boolean predict(List data) {
        // Do prediction
        return false;
    }

    public void trainClassifier(List data) {
        // Do something here
    }

    public String getName() {
        return this.name;
    }
}

public class NaiveBayesClassifier extends Classifier {
    public NaiveBayesClassifier() {
        super("NaiveBayesClassifier");
    }
}

public class SMOClassifier extends Classifier {
    public SMOClassifier() {
        super("SMOClassifier");
    }
}

public class Main {
    public static void main(String[] args) {
        List<Classifier> classifiers = new ArrayList<>();
        classifiers.add(new SMOClassifier());
        classifiers.add(new NaiveBayesClassifier());

        for (Classifier c : classifiers) {
            System.out.println(c.getName());
        }
    }
}
```

```cpp
#include <string>
#include <iostream>

using namespace std;

class Classifier {
public:
    string name;

    Classifier(string name) {
        this->name = name;
    }

    virtual void getName() {
        cout << this->name << endl;
    };
};

class NaiveBayesClassifier : public Classifier {
public:
    NaiveBayesClassifier() : Classifier("NaiveBayesClassifier") {

    };
};

class SMOClassifier : public Classifier {
public:
    SMOClassifier() : Classifier("SMOClassifier") {
        
    };
};

void show_name(Classifier *c) {
    c->getName();
}

int main(void) {
    NaiveBayesClassifier nbc;
    SMOClassifier smoc;

    show_name(&nbc);
    show_name(&smoc);

    return 0;
}
```


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

http://openhome.cc/Gossip/Python/TryRaise.html
https://docs.python.org/3.4/tutorial/errors.html


---

# 模組的概念 Module

https://docs.python.org/3.4/tutorial/modules.html
http://blog.eddie.com.tw/2011/10/13/python-module/
http://www.codedata.com.tw/python/python-tutorial-the-2nd-class-3-function-module-class-package/
http://pydoing.blogspot.tw/2011/02/python-module.html


---

# 撰寫文件 Documentation by pydoc and sphinx

http://www.sphinx-doc.org/en/stable/tutorial.html
http://chimerhapsody.blogspot.tw/2014/07/python.html
https://www.ibm.com/developerworks/cn/opensource/os-sphinx-documentation/
http://www.sphinx-doc.org/en/stable/ext/autodoc.html


---

# 單元測試 Unit Test

http://www.codedata.com.tw/python/python-tutorial-the-6th-class-1-unittest/
https://docs.python.org/3.4/library/unittest.html


---

# 其他滿有用的概念：檔案讀寫與參數傳遞 File I/O and Argument Passing

## File I/O

https://docs.python.org/3.4/tutorial/inputoutput.html#reading-and-writing-files

## Argument

https://docs.python.org/3.4/howto/argparse.html#id1
https://docs.python.org/3.4/library/argparse.html


---

# Git & GitHub

https://ihower.tw/git/index.html
http://gogojimmy.net/2012/01/17/how-to-use-git-1-git-basic/
http://www.ithome.com.tw/news/95283
https://try.github.io/levels/1/challenges/1


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

