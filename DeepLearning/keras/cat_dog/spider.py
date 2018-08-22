import re
import requests
import os


# 爬取图片网址
def getManyPages(keyword,pages):
    params=[]
    header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    for i in range(30,30*pages+30,30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1488942260214': ''
                  })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        try:
            urls.append(requests.get(url,params=i, headers=header).json().get('data'))
        except Exception as e:
            print(e)
    return urls


# 爬取图片
def getImg(dataList, localPath):
    x = 0
    for list in dataList:
        for i in list:
            try:
                if i.get('thumbURL') != None:
                    print('正在下载：%s' % i.get('thumbURL'))
                    ir = requests.get(i.get('thumbURL'))
                    open(localPath + '/' + '%d.jpg' % x, 'wb').write(ir.content)
                    x += 1
                else:
                    print('图片链接不存在')
            except Exception as e:
                print(e)


if __name__ == '__main__':
    # 分类
    name = '狗'
    path =os.getcwd() + '/images/train/dog'
    dataList = getManyPages(name, 10)  # 参数1:关键字，参数2:要下载的页数
    getImg(dataList, path)  # 参数2:指定保存的路径



