import requests  # 发送请求
from bs4 import BeautifulSoup  # 解析网页
import pandas as pd  # 存取csv
from time import sleep  # 等待时间

movie_name = []  # 电影名称
movie_url = []  # 电影链接
movie_star = []  # 电影评分
movie_star_people = []  # 评分人数
movie_director = []  # 导演
movie_actor = []  # 主演
movie_year = []  # 上映年份
movie_country = []  # 国家
movie_type = []  # 类型


def get_movie_info(url, headers):

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    for movie in soup.select('.item'):
        name = movie.select('.hd a')[0].text.replace('\n', '')  # 电影名称
        movie_name.append(name)
        url = movie.select('.hd a')[0]['href']  # 电影链接
        movie_url.append(url)
        star = movie.select('.rating_num')[0].text  # 电影评分
        movie_star.append(star)
        star_people = movie.select('.star span')[3].text  # 评分人数
        star_people = star_people.strip().replace('人评价', '')
        movie_star_people.append(star_people)
        movie_infos = movie.select('.bd p')[0].text.strip()  # 导演、主演、年份、国家、类型
        director = movie_infos.split('\n')[0].split('   ')[0]
        movie_director.append(director)
        try:  # 页面上既有导演，又有主演
            actor = movie_infos.split('\n')[0].split('   ')[1]
            movie_actor.append(actor)
        except:  # 页面上只有导演，没有主演
            movie_actor.append(None)
        if name == '大闹天宫 / 大闹天宫 上下集  /  The Monkey King':  # 大闹天宫，特殊处理
            year0 = movie_infos.split('\n')[1].split('/')[0].strip()
            year1 = movie_infos.split('\n')[1].split('/')[1].strip()
            year2 = movie_infos.split('\n')[1].split('/')[2].strip()
            year = year0 + '/' + year1 + '/' + year2
            movie_year.append(year)
            country = movie_infos.split('\n')[1].split('/')[3].strip()
            movie_country.append(country)
            type = movie_infos.split('\n')[1].split('/')[4].strip()
            movie_type.append(type)
        else:  # 其他电影，正常处理
            year = movie_infos.split('\n')[1].split('/')[0].strip()
            movie_year.append(year)
            country = movie_infos.split('\n')[1].split('/')[1].strip()
            movie_country.append(country)
            type = movie_infos.split('\n')[1].split('/')[2].strip()
            movie_type.append(type)


def save_to_csv(csv_name):

    df = pd.DataFrame()  # 初始化一个DataFrame对象
    df['电影名称'] = movie_name
    df['电影链接'] = movie_url
    df['电影评分'] = movie_star
    df['评分人数'] = movie_star_people
    df['导演'] = movie_director
    df['主演'] = movie_actor
    df['上映年份'] = movie_year
    df['国家'] = movie_country
    df['类型'] = movie_type
    df.to_csv(csv_name, encoding='utf_8_sig')  # 将数据保存到csv文件


if __name__ == "__main__":
    # 定义一个请求头(防止反爬)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    # 开始爬取豆瓣数据
    for i in range(10):  # 爬取共10页，每页25条数据
        page_url = 'https://movie.douban.com/top250?start={}'.format(str(i * 25))
        print('开始爬取第{}页，地址是:{}'.format(str(i + 1), page_url))
        get_movie_info(page_url, headers)
        sleep(1)  # 等待1秒(防止反爬)
    # 保存到csv文件
    save_to_csv(csv_name="MovieDouban250.csv")
