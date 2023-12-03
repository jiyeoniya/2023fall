# 关于招聘网站的相关数据分析

## 目录：
1. [分析背景](#jump1)

2. [爬取数据并存储为csv文件和mysql数据库中](#jump2)
   
3. [数据清洗](#jump3)
   
4. [数据分析于可视化](#jump4)
   
5. [总结](#jump5)

## <span id="jump1">1. 分析背景</span>

  当今社会，随着互联网的普及和发展，招聘行业也逐渐倾向于在线化。越来越多的企业借助互联网招聘平台发布岗位信息，并通过网络筛选和面试候选人。招聘数据爬虫及数据分析可视化大屏技术应运而生，成为了提高招聘效率、优化人才资源配置的重要手段之一。
  传统的招聘方式需要耗费大量时间和人力，效率低下。而在线招聘平台的出现可以大大提高招聘效率，减少人力成本。但是，由于网络上的海量信息，如何从中筛选出符合要求的招聘信息和候选人仍然是一个挑战。因此，开发一种招聘数据爬虫及数据分析可视化大屏技术，将有助于更快速、更准确地获取和分析招聘信息。


## <span id="jump2">2.爬取数据</span>

### （1）导入所需的库

    from selenium import webdriver #浏览器自动化库
    from selenium.webdriver.support.ui import WebDriverWait #等待库
    from bs4 import BeautifulSoup #解析网页html文件
    import pymysql #mysql数据库操作库
    import random #生成随机数的库
    import requests #请求库
    from fake_useragent import UserAgent #User-Agent伪装库

### （2）定义一个函数，将数据存入数据库store_data
### （3）连接数据库，获取游标
### （4）开启无头浏览器
    driver = webdriver.Chrome('edgedriver.exe') #打开Chrome浏览器
    base_url = "https://www.zhipin.com" #定义基础url
### （5）每个城市爬取
    for city in citys:
      urls = ['https://www.zhipin.com/c{}-p100109/?page={}&ka=page-{}'.format(city['code'], i, i) for i in range(10, 11)] #定义城市的url

    for url in urls:
    driver.get(url) #打开url

    html = driver.page_source #获取网页源代码
    bs = BeautifulSoup(html, 'html.parser') #解析html文件

    job_all = bs.find_all('div', {"class": "job-primary"}) #查找工作信息

    for job in job_all:
        # 工作名称
        job_name = job.find('span', {"class": "job-name"}).get_text()
        # 工作地点
        job_place = job.find('span', {'class': "job-area"}).get_text()
        # 工作公司
        job_company = job.find('div', {'class': 'company-text'}).find('h3', {'class': "name"}).get_text()
        # 工作薪资
        job_salary = job.find('span', {'class': 'red'}).get_text()
        # 工作学历
        job_education = job.find('div', {'class': 'job-limit'}).find('p').get_text()[-2:]
        # 工作标签
        job_label = job.find('a', {'class': 'false-link'}).get_text()
        # 招聘详情页链接
        job_url = base_url + job.find('div', class_="company-text").a.attrs['href']
        # 工作经验
        job_experience = job.find('div', {'class': 'job-limit clearfix'}).find('p').get_text()[:-2]
        
        # 存储到数据库
        store_data(job_name, job_place, job_company, job_salary, job_education, job_label, job_url, job_experience,
                   conn, cursor)
        
        with open('cd.csv', 'a+', encoding='UTF-8-SIG') as fh:
            # 处理避免读取歧义
            fh.write(job_name.replace(',',
                                      '、') + "," + job_place + "," + job_company + "," + job_salary + "," + job_education + ',' + job_label + ',' + job_url +',' + job_experience +"\n")

            # 检验成功写入、并成功获取数据
            print(
                '工作:' + job_name + "，地区:" + job_place + ",公司:" + job_company + ",薪资:" + job_salary + ',学历:' + job_education + ",标签:" + job_label + "，链接:" + job_url + ",经验:" + job_experience,
                end="\n")
### （6）关闭无头浏览器，减少内存损耗
    driver.quit() #关闭Chrome浏览器

### (7)存储为csv文件和mysql数据库中

如下图所示：

![](https://github.com/jiyeoniya/2023fall/blob/main/LastProject/resultPIc/mysql1.png "")

## <span id="jump3">3.数据清洗</span>

### （1）
  首先，使用pandas库读取“job.csv”文件并转化为数据框df。然后，使用matplotlib库调整显示中文标签的设置，来保证后续绘图的中文显示正常。接着，使用isnull().sum()函数，分别查看每一列是否含有缺失值。
    
    data = pd.read_csv('job.csv')
    df = pd.DataFrame(data)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 设置正常显示符号
    pd.set_option('max_colwidth',100)
    df.head()
### （2）
  根据需求筛选出带有“元”单位的行，然后分别提取区间最小薪资和区间最大薪资，并将其加入到数据框df的合适位置。再接着，提取工作地点的城市信息，然后也将其加入到数据框df的合适位置。
  例如：

    # 工作城市
    df_city = df['工作地点'].str.split('·', expand=True)[0]
    print(df_city)  # 城市
    # Dataframe新增一列  在第 列新增一列名为' ' 的一列 数据
    df.insert(1, '工作城市', df_city)
    print(df)
    
### （3）
  之后，计算出每个工作的平均薪资，并将其加入到数据框df的合适位置。接着，将工作经验的描述信息中冗余的内容进行清除，并进行统一的标准化处理。最后，将清洗后的数据保存到“job_clean.csv”文件中。
    
    df.to_csv("job_clean.csv",encoding = "utf_8_sig")
  
  通过对比“job.csv”和“job_clean.csv”两份文件，可以发现“job_clean.csv”文件更规范、更易于处理和分析。

![](https://github.com/jiyeoniya/2023fall/blob/main/LastProject/resultPIc/before.png "")
![](https://github.com/jiyeoniya/2023fall/blob/main/LastProject/resultPIc/clean.png "")
## <span id="jump4">4.数据分析与可视化</span>

### 有做很多其他的数据可视化大屏，最后也有用html整合为一个可视化网站，但在下面只列出三种：

### （1）针对各城市工资的分析
  首先使用 pandas 库中的 groupby() 方法对一个名为 df 的数据框按照列名为 '工作城市' 的列进行分组，并计算每组中另一列名为 '平均工资(K)' 的数值型变量的平均值，最小值和最大值。

    average_salary = df.groupby('工作城市')['平均工资(K)'].mean()#平均工资
    average_low_salary = df.groupby('工作城市')['最小薪资(K)'].mean()#最低平均工资
    average_high_salary = df.groupby('工作城市')['最大薪资(K)'].mean()#最高平均工资
  然后将这三个值分别存储在 y1、y2 和 y3 中，x 存储 '工作城市' 列的唯一值。
      
    y1 = average_salary.reset_index()['平均工资(K)'].tolist()
    y2 = average_low_salary.reset_index()['最小薪资(K)'].tolist()
    y3 = average_high_salary.reset_index()['最大薪资(K)'].tolist()
  接着创建一个 Bar 对象 bar，设置其初始化选项 init_opts 包括宽度、高度和主题等参数。然后使用 add_xaxis() 和 add_yaxis() 方法向柱状图中添加 x 和 y 坐标轴以及相应的数据。
    
    bar.add_xaxis(x)
    bar.add_yaxis("各城市平均工资", y1)
    bar.add_yaxis("各城市最低平均工资", y2)
    bar.add_yaxis("各城市最高平均工资", y3)
  使用 set_series_opts() 方法设置柱状图上的标签不显示数字。

    bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))#不显示数字
    
  使用 set_global_opts() 方法设置工具箱、标题、纵坐标和横坐标等参数。

    bar.set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                    title_opts=opts.TitleOpts(title="各城市工资"),
                    yaxis_opts=opts.AxisOpts(name="薪资(K)"),
                    xaxis_opts=opts.AxisOpts(name="城市",axislabel_opts=opts.LabelOpts(rotate=-50))#旋转x轴内容
                   )
  最后调用 render() 方法将图表保存为一个 各城市工资。
    
    # datazoom_opts=opts.DataZoomOpts()#滚动条
    bar.render("各城市工资.html")

   最后得到如下所示：
   ![](https://github.com/jiyeoniya/2023fall/blob/main/LastProject/resultPIc/%E5%90%84%E5%AD%A6%E5%8E%86%E5%B7%A5%E8%B5%84.png "") 
### （2）针对评价词云的分析

  方法与上述类似，首先使用 pandas 库中的 groupby() 方法对一个名为 df 的数据框按照列名为 '工作标签' 的列进行分组，并计算每组中另一列名为 '平均工资(K)' 的数值型变量的数量。 然后将每个标签及其出现次数分别存储在 tags 和 value 中。
    
    tag_count = df.groupby('工作标签')['平均工资(K)'].count()#平均工资
    print(tag_count.reset_index()['工作标签'].tolist())
    print(tag_count.reset_index()['平均工资(K)'].tolist())
    tags = tag_count.reset_index()['工作标签'].tolist()
    value = tag_count.reset_index()['平均工资(K)'].tolist()
  接着使用列表推导式创建一个包含元组的列表 data_pair，其中每个元组包括一个标签和该标签出现的次数。

    data_pair=[(i,j) for i,j in zip(tags, value)]
  创建一个 WordCloud 对象 mywordcloud，设置其初始化选项 init_opts 包括宽度、高度等参数。

    mywordcloud = WordCloud(init_opts=opts.InitOpts(width='1000px',height='600px'))
  使用 add() 方法向词云图中添加标签及其出现次数数据。

    mywordcloud.add('',data_pair, shape='circle')
  使用 set_global_opts() 方法设置工具箱、标题等参数。

    mywordcloud.set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                            title_opts=opts.TitleOpts(title="WordCloud-图片"))
  最后调用 render() 方法将词云图保存为一个 HTML 文件，文件名为 'WordCloud-图片'。

    mywordcloud.render("WordCloud-图片.html")

最后得到如下所示：
   ![](https://github.com/jiyeoniya/2023fall/blob/main/LastProject/resultPIc/%E8%AF%8D.png "") 

### （3）针对学历占比的分析
  知道了上面两种如何分析，之后就很容易了。首先使用 pandas 库中的 groupby() 方法对一个名为 df 的数据框按照列名为 '工作学历' 的列进行分组，并计算每组中另一列名为 '平均工资(K)' 的数值型变量的数量。然后将每个学历及其出现次数分别存储在 attr 和 value 中。然后使用列表推导式创建一个包含元组的列表 data_pair，其中每个元组包括一个学历和该学历出现的次数。

    experience_count = df.groupby('工作学历')['平均工资(K)'].count()#平均工资
    print(experience_count.reset_index()['工作学历'].tolist())
    print(experience_count.reset_index()['平均工资(K)'].tolist())
    attr = experience_count.reset_index()['工作学历'].tolist()
    value = experience_count.reset_index()['平均工资(K)'].tolist()
  创建一个 Pie 对象 pie，设置其初始化选项 init_opts 包括宽度、高度和主题等参数。

    pie = Pie(init_opts=opts.InitOpts(width='800px',height='400px',theme=ThemeType.MACARONS))
  使用 add() 方法向饼图中添加学历及其出现次数数据。

    pie.add(series_name='',data_pair=[(i,j) for i,j in zip(attr, value)])
  使用 set_global_opts() 方法设置工具箱、标题等参数。

    pie.set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                    title_opts=opts.TitleOpts(title="学历要求占比"))
  使用 set_series_opts() 方法设置标签格式，其中 {b} 表示数据项名称，{d}% 表示数据项所占比例（保留一位小数）。最后调用 render() 方法将饼图保存为一个 HTML 文件，文件名为 学历要求占比

    pie.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}%'))
    pie.render("学历要求占比.html")

最后得到如下所示：
   ![](https://github.com/jiyeoniya/2023fall/blob/main/LastProject/resultPIc/%E5%AD%A6%E5%8E%86%E8%A6%81%E6%B1%82%E5%8D%A0%E6%AF%94.png "") 

 ## <span id="jump5">5.总结</span>

  在招聘市场日趋竞争的今天，企业和应聘者需要通过各种渠道获取更多的招聘信息，以便更好地了解市场动态、提高招聘效率和准确性。

  因此，招聘数据爬虫成为了一种重要的工具，可以帮助企业和应聘者快速采集招聘信息并进行分析。同时，数据可视化也成为了另一个重要的工具，可以让企业和招聘者更直观地了解招聘市场动态，进而制定更科学的招聘策略。



