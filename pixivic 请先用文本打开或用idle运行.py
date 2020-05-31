import re
import requests
import json

"""
本程序针对于 https://pixivic.com/  （第三方p站图库）
python版本：3.8.1
原作者qq：3028799143
欢淫交流[坏笑]
长时间无反应可能是官方服务器问题
"""
#   爬完一次了 url 自己调，把page往后条就行了，还有那个日期
url = 'https://api.pixivic.com/ranks?page=1&date=2020-05-29&mode=day&pageSize=30'
headers = {'access-control-allow-origin': 'https://pixivic.com',
           'referer': 'https://pixivic.com/?VNK=94e3d6d3'}
print("程序已缓冲好")
print("如果较长时间没有响应（可能是官方服务器问题），请过一段时间重试或访问\nhttps://pixivic.com/")
print('本程序仍然可能存在下载了漫画的情况，所以还请见谅')


def img(urls):               # 首先做一个单个原图爬取的爬虫
    if ''.join(re.findall('net', urls)) == 'net':       # 这个是用来判断是否是填的p站链接（其实只有这个）
        # 如果是p站链接
        urls = urls.replace('https://i.pximg.net', 'https://original.img.cheerfun.dev')
    print(urls)
    referer = ''.join(re.findall('dev/.*?/.*?/.*?/.*?/.*?/.*?/.*?/.*?/(.*?g)', urls))
    print(referer)
    header = {'referer': 'https://pixivic.com/illusts/'+referer+'?VNK=83de5ca0',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    res = requests.get(urls, headers=header)
    opens = 'C:\\Users\\kuang\\PycharmProjects\\untitled2\\代码库\\爬虫\\图片\\'+referer
    #   填你自己的
    c = open(opens, 'wb')
    c.write(res.content)


def our_30(urls):       # 每30个链接的爬取
    res = requests.get(url, headers=headers)
    all_url = []
    # 通过json获取到所有少于4张的链接
    for i in json.loads(res.text)['data']:
        if i['pageCount'] <= 4:
            c = re.findall("original': '(ht.*?)'}", str(i['imageUrls']))
            all_url.append(c)
    for a in all_url:
        # 输出的是一串列表，所以要再次循环
        for c in a:
            img(c)

    print(len(all_url))


'''    for i in 非全部链接:
        if i not in good_list and i in rf:
            if i not in 全部链接:
                全部链接.append(i)
    for a in 全部链接:
        img(a)'''



'''
    for a in rf:
        img(a)'''





"""
这里是对比
原 ：https://original.img.cheerfun.dev/img-original/img/2020/05/13/00/25/13/81519867_p0.jpg
小： https://img.cheerfun.dev:233/c/540x540_70/img-master/img/2020/05/13/00/25/13/81519867_p0_master1200.jpg
                        https://i.pximg.net/img-original/img/2020/05/13/02/26/19/81522430_p0.png
        https://original.img.cheerfun.dev/img-original/img/2020/05/13/02/26/19/81522430_p0.png
"""
if __name__ == '__main__':
    our_30(url)
