from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup
import pymysql
import random
import requests
from fake_useragent import UserAgent


def store_data(job_name1, job_place1, job_company1, job_salary1, job_education1, job_label1, job_url1, job_experience1, conn, cursor):
    try:
        cursor.execute(
            'insert into job_data (job_name,job_place,job_company,job_salary,job_education,job_label,job_url,job_experience) '
            'values ("{}","{}","{}","{}","{}","{}","{}","{}")'.format(job_name1, job_place1, job_company1,
                                                                           job_salary1, job_education1,
                                                                           job_label1, job_url1,
                                                                           job_experience1))
    except:
        print("存入数据库失败")

    conn.commit()
conn = pymysql.connect(
    host="localhost",
    user="root", password="pizhya0817",
    database="job_data",
    charset="utf8")
cursor = conn.cursor()
# 无头浏览器开启
edge_driver_path = "edgedriver.exe"
edge_service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=edge_service)
base_url = "https://www.zhipin.com"
# 城市json
citys = [{"name": "北京", "code": 101010100, "url": "/beijing/"},{"name": "上海", "code": 101020100, "url": "/shanghai/"},
         {"name": "广州", "code": 101280100, "url": "/guangzhou/"},{"name": "贵阳", "code": 101260100, "url": "/guiyang/"},
         {"name": "深圳", "code": 101280600, "url": "/shenzhen/"}, {"name": "杭州", "code": 101210100, "url": "/hangzhou/"},
         {"name": "天津", "code": 101030100, "url": "/tianjin/"}, {"name": "西安", "code": 101110100, "url": "/xian/"},
         {"name": "苏州", "code": 101190400, "url": "/suzhou/"}, {"name": "武汉", "code": 101200100, "url": "/wuhan/"},
         {"name": "厦门", "code": 101230200, "url": "/xiamen/"}, {"name": "长沙", "code": 101250100, "url": "/changsha/"},
         {"name": "成都", "code": 101270100, "url": "/chengdu/"}, {"name": "郑州", "code": 101180100, "url": "/zhengzhou/"},
         {"name": "重庆", "code": 101040100, "url": "/chongqing/"},{"name": "海口", "code": 101310100, "url": "/haikou/"},
         {"name": "合肥", "code": 101220100, "url": "/hefei/"}, {"name": "济南", "code": 101120100, "url": "/jinan/"},
         {"name": "青岛", "code": 101120200, "url": "/qingdao/"}, {"name": "南京", "code": 101190100, "url": "/nanjing/"},
         {"name": "呼和浩特", "code": 101080100, "url": "/huhehaote/"}]

# 每个城市爬取
for city in citys:
    urls = ['https://www.zhipin.com/c{}-p100109/?page={}&ka=page-{}'.format(city['code'], i, i) for i in
            range(10, 11)]

    for url in urls:
        # chromeOptions = webdriver.ChromeOptions()
        #
        # ip_list = ["47.110.135.140"]
        # port_list = ["8118"]
        # index = random.randint(0, len(ip_list) - 1)
        # ip = ip_list[0]
        # port = port_list[0]
        # # 设置代理
        # chromeOptions.add_argument("--proxy-server=http://{}:{}".format(ip, port))
        # driver = webdriver.Chrome(chrome_options=chromeOptions)
        # headers = {
        #     'User - Agent': UserAgent().random,
        # }
        # chromeOptions.add_argument('user-agent=ywy')
        # driver = webdriver.Chrome(options=chromeOptions)
        # 最大等待时间10s
        # wait = WebDriverWait(driver, 10)

        driver.get(url)

        # 获取源码，解析
        html = driver.page_source
        bs = BeautifulSoup(html, 'html.parser')

        job_all = bs.find_all('div', {"class": "job-primary"})
        # print(job_all)

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
            # 注：csv编码需更改为utf-8(若编码不为UTF-8）另：下载后需用记事本打开再另存为时将编码改为带BOM的UTF-8格式
            with open('cd.csv', 'a+', encoding='UTF-8-SIG') as fh:
                # 处理避免读取歧义
                fh.write(job_name.replace(',',
                                          '、') + "," + job_place + "," + job_company + "," + job_salary + "," + job_education + ',' + job_label + ',' + job_url +',' + job_experience +"\n")

                # 检验成功写入、并成功获取数据
                print(
                    '工作:' + job_name + "，地区:" + job_place + ",公司:" + job_company + ",薪资:" + job_salary + ',学历:' + job_education + ",标签:" + job_label + "，链接:" + job_url + ",经验:" + job_experience,
                    end="\n")


# 关闭无头浏览器，减少内存损耗
driver.quit()