# WEEK5 H.W. REPORT

## 第一题：

### Q:下载安装并配置一个数据库,例如 MySQL、PostgreSQL

#### A：MySQL为非常常用的一种数据库，故本人安装了MySQL。

## 第二题：

### Q:新建一个用户,再新建一个数据库，赋予新用户可操作该数据库的所有权限。

#### A：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/3.png "")

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/2.png "")

## 第三题：

### Q:在新数据库中新建一张 user 表,插入几条数据,属性包含:唯一标识(id),姓名(name),性别(sex),年龄(age),联系方式(phone)。

#### A：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/4.png "")

## 第四题：

### Q:写出 SQL语句,查询 user 表中所有年龄在 20-30 范围内的用户

#### A：先执行以下语句来抓取所有表格数据，发现表格内容是空的

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/5.png "")

于是，插入若干个数据：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/6.png "")
![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/7.png "")
![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/8.png "")

然后在执行查询 user 表中所有年龄在 20-30 范围内的用户的语句得出：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/9.png "")

## 第五题：

### Q:写出 SQL语句,删除 user 表中名字包含“张”的用户

#### A：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/14.png "")

## 第六题：

### Q:写出 SQL 语句,计算 user 表中所有用户的平均年龄

#### A：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/15.png "")

## 第七题：

### Q:写出 SQL语句,查询 user 表中年龄在 20-30 范围内,名字包含“张”的用户,并按照年龄从大到小排序输出。

#### A：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/16.png "")

## 第八题：

### Q:新建两张表,team 表(id,teamName),score 表(id,teamid,userid,score)。
### 其中，score 表中的 teamid 为指向 team 表 id 的外键,userid 为指向 user 表 id 的外键

#### A：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/17.png "")

为了执行下面两道题的语句，现在向这两个新建的表中插入若干个数据：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/18.png "")


## 第九题：

### Q:写出 SQL 语句，查询 teamName 为“ECNU”的队伍中,年龄小于 20 的用户们。

#### A：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/20.png "")

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/21.png "")

## 第十题：

### Q:写出 SQL 语句,计算 teamName 为“ECNU”的总分(假设 score 存在 null 值,null值默认为 0加入计算)。

#### A：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/19.png "")

## 第一题：

### Q:修改 6.7.1 实验代码,实现将爬取数据保存到数据库当中

#### A：由于本人数据库被安装在D盘，需要一系列其他操作，将在后续的期末大项目中进行并补充说明。于是，本人还是将爬取数据存入一个csv文件中。爬取结果如下：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/douban.png "")

## 第二题：

### Q:熟悉爬虫的 scrapy 框架,并且自己动手安装。了解该框架的优缺点

#### A：

Scrapy是一个用Python编写的强大的网络爬虫框架，它可以快速地从各种网站提取结构化的数据。
Scrapy 是用 Python 实现的一个为了爬取网站数据、提取结构性数据而编写的应用框架。
Scrapy 常应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。
通常我们可以很简单的通过 Scrapy 框架实现一个爬虫，抓取指定网站的内容或图片。(来源：菜鸟教程)

#### Scrapy架构图(绿线是数据流向)
![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/scrapy.png "")

Scrapy Engine(引擎): 负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等。

Scheduler(调度器): 它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎。

Downloader（下载器）：负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine(引擎)，由引擎交给Spider来处理，

Spider（爬虫）：它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器).

Item Pipeline(管道)：它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方。

Downloader Middlewares（下载中间件）：你可以当作是一个可以自定义扩展下载功能的组件。

Spider Middlewares（Spider中间件）：你可以理解为是一个可以自定扩展和操作引擎和Spider中间通信的功能组件（比如进入Spider的Responses;和从Spider出去的Requests）

#### Scrapy的运作流程

代码写好，程序开始运行...

1 引擎：Hi！Spider, 你要处理哪一个网站？

2 Spider：老大要我处理xxxx.com。

3 引擎：你把第一个需要处理的URL给我吧。

4 Spider：给你，第一个URL是xxxxxxx.com。

5 引擎：Hi！调度器，我这有request请求你帮我排序入队一下。

6 调度器：好的，正在处理你等一下。

7 引擎：Hi！调度器，把你处理好的request请求给我。

8 调度器：给你，这是我处理好的request

9 引擎：Hi！下载器，你按照老大的下载中间件的设置帮我下载一下这个request请求

10 下载器：好的！给你，这是下载好的东西。（如果失败：sorry，这个request下载失败了。然后引擎告诉调度器，这个request下载失败了，你记录一下，我们待会儿再下载）

11 引擎：Hi！Spider，这是下载好的东西，并且已经按照老大的下载中间件处理过了，你自己处理一下（注意！这儿responses默认是交给def parse()这个函数处理的）

12 Spider：（处理完毕数据之后对于需要跟进的URL），Hi！引擎，我这里有两个结果，这个是我需要跟进的URL，还有这个是我获取到的Item数据。

13 引擎：Hi ！管道 我这儿有个item你帮我处理一下！调度器！这是需要跟进URL你帮我处理下。然后从第四步开始循环，直到获取完老大需要全部信息。

14 管道调度器：好的，现在就做！

注意！只有当调度器中不存在任何request了，整个程序才会停止，（也就是说，对于下载失败的URL，Scrapy也会重新下载。）

#### 制作 Scrapy 爬虫 一共需要4步：

新建项目 (scrapy startproject xxx)：新建一个新的爬虫项目

明确目标 （编写items.py）：明确你想要抓取的目标

制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页

存储内容 （pipelines.py）：设计管道存储爬取内容

#### 安装Scrapy：

在Python环境中，可以使用pip工具安装Scrapy。以下是在命令行中进行安装的指令：

`pip install scrapy`

#### 以下是Scrapy的一些主要优点和缺点。

#### 优点：

1.易用性：Scrapy具有很高的易用性，它提供了简洁的API和明确的工作流程，使得开发者可以轻松地编写出高效的爬虫。

2.灵活性：Scrapy具有很高的灵活性，它支持各种类型的爬虫，包括简单和复杂的。此外，它还可以轻松地与各种数据库和中间件进行集成。

3.异步处理：Scrapy采用了Twisted网络库作为其底层支撑，支持异步I/O操作，使得数据处理和网络请求可以并发进行，提高了爬虫的效率。

4.可扩展性：Scrapy具有很好的可扩展性，它支持插件系统，可以通过编写自定义的插件来扩展其功能。

5.调试方便：Scrapy提供了丰富的调试工具，使得开发者可以轻松地定位和解决遇到的问题。

#### 缺点：

1.学习曲线：虽然Scrapy的API和文档都非常友好，但是对于初学者来说，理解和掌握它可能需要一些时间。

2.依赖性：Scrapy依赖于Twisted网络库和一些第三方库，这可能会增加部署和运行的复杂性。

3.不支持移动端：由于Scrapy主要是为PC网页设计的，因此在处理移动端网页时可能会遇到问题。

4.无法处理动态内容：Scrapy主要处理的是静态网页内容，对于需要处理动态生成或JavaScript生成内容的网页来说，可能会力不从心。

## 第三题：

### Q:用 scrapy 框架初始化一个简单的爬虫项目,并且熟悉项目各个架构代码

#### A：下面两道题也是一个用scrapy框架制作一个爬虫项目，请直接移步下面。

## 第四题：

### Q:用 scrapy 框架爬取当当网计算机类书籍信息的首页。

#### A：初步爬取了关键字为“计算机”的一些书籍的书名，价格以及其他相关信息将在后续项目中进行类似操作。

## 第五题：

### Q:在习题 4 的基础上，自动爬取该类书籍的所有信息页面

#### A：初步爬取了关键字为“计算机”的一些书籍的书名，价格以及其他相关信息将在后续项目中进行类似操作。得到的csv文件如下所示：

![](https://github.com/jiyeoniya/2023fall/blob/main/week5/ProPics/dangdang.png "")
