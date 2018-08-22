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
    
    # l = ['bus', 'dinosaurs', 'elephants', 'flowers', 'horse']
    # 创建文件夹
    # l = ['恐龙']
    # for i in  l:
    #     path = './re/validation1/dinosaurs'
    #     if not os.path.exists(path):
    #         os.mkdir(path)
    #         print(i)
    #         dataList = getManyPages(i, 1)  # 参数1:关键字，参数2:要下载的页数
    #         getImg(dataList, path)  # 参数2:指定保存的路径

    
    # path = './re/validation1/flowers'
    # dataList = getManyPages('花',1)
    # getImg(dataList, path)




#真本
data = {
	'error':None,
 	'corver': 0.99,
 	'texture': 160000,
 	'font': 0.95,
 	'charecter': True,
 	'conclusion': 4
 }   


# 假本
 data = {
 	'error':None,
 	'corver': 0.1,
 	'texture': None,
 	'font': None,
 	'charecter': None,
 	'conclusion': 0
 }

# 分辨率不合格
 data ={
 	'error':None,
 	'corver': None,
 	'texture': None,
 	'font': None,
 	'charecter': None,
 	'conclusion': -1
 }

# 真本无抵押信息或未检测出字体
 data ={
 	'error': None,
 	'corver': 0.95,
 	'texture': 210000,
 	'font': ‘未检测’,
 	'charecter': None,
 	'conclusion': 2
 }

