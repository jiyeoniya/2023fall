# 关于招聘网站的相关数据分析

## 目录：
## 1.分析背景
## 2.爬取数据
## 3.数据分析
## 4.数据可视化

## 1.分析背景



## 2.爬取数据

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
    driver = webdriver.Chrome('chromedriver.exe') #打开Chrome浏览器
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
