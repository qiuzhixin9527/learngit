import cv2
import os
import matplotlib.pyplot as plt
from sklearn import preprocessing

import numpy as np


def normalization(img):
    print(type(img))
    origin_min = img.min()
    origin_max = img.max()
    origin_range = origin_max - origin_min
    print('+++++++++++++++++++++++')
    print(origin_range)

    target_min = 0
    target_max = 255
    target_range = target_max - target_min

    return (255*((img - origin_min)/origin_range)).astype(np.uint8)


white_file_url = '/home/chenm/Documents/shiqiao/cover_classifier/dataset/黑白扫描/白'
black_file_url = '/home/chenm/Documents/shiqiao/cover_classifier/dataset/黑白扫描/黑'

white_file_list = [os.path.join(white_file_url, file) for file in os.listdir(white_file_url)]
black_file_list = [os.path.join(black_file_url, file) for file in os.listdir(black_file_url)]

print(white_file_list)
print(black_file_list)

#白
for url_white, url_black in zip(white_file_list,black_file_list):
    rgb_img_white = cv2.imread(url_white)

    rgb_img_white = rgb_img_white[5000:5224, 2000:2224]
    # print(type(rgb_img_white))

    # B, G, R = cv2.split(rgb_img_white)
    HSV_white = cv2.cvtColor(rgb_img_white, cv2.COLOR_BGR2HSV)

    H_white, S_white, V_white = cv2.split(HSV_white)




    # aa = (V_white-V_white.mean())/V_white.std()
    #
    # I_white = (B + G + R) // 3
    #
    eq_white = cv2.equalizeHist(V_white)
    #
    # print(I_white)
    # plt.imshow(H_white)
    # plt.show()
    # plt.imshow(S_white)
    # plt.show()
    V_white = normalization(V_white)

    # HSV_white[:, :, 2] = V_white

    rgb_img_white = cv2.cvtColor(HSV_white, cv2.COLOR_HSV2RGB)


    # plt.imshow(V_white)
    # plt.show()
    # plt.imshow(eq_white)
    # plt.show()
    plt.imshow(rgb_img_white)
    plt.show()




    # 黑
    rgb_img_black = cv2.imread(url_black)
    rgb_img_black = rgb_img_black[5000:5224, 2000:2224]
    # B, G, R = cv2.split(rgb_img_black)

    HSV_black = cv2.cvtColor(rgb_img_black, cv2.COLOR_BGR2HSV)
    H_black, S_black, V_black = cv2.split(HSV_black)

    # I_black = (B + G + R) // 3
    #
    eq_black = cv2.equalizeHist(V_black)
    # plt.imshow(H_black)
    # plt.show()
    # plt.imshow(S_black)
    # plt.show()
    # plt.imshow(V_black)
    # plt.show()
    V_black = normalization(V_black)

    # HSV_black[:, :, 2] = V_black

    rgb_img_black = cv2.cvtColor(HSV_black, cv2.COLOR_HSV2RGB)


    # print(V_black)
    print('!!!!!!!!!!!!!!!!!!!!!!!!')
    print(V_black.max())
    print(V_black.min())

    # plt.imshow(V_black)
    # plt.show()
    # plt.imshow(eq_black)
    # plt.show()
    plt.imshow(rgb_img_black)
    plt.show()

    print('白扫描仪H均值:', round(H_white.mean(),5), '\t', '黑扫描仪H均值:', round(H_black.mean(),5),'比例:',round(H_white.mean()/H_black.mean(),5))
    print('白扫描仪S均值:', round(S_white.mean(),5), '\t', '黑扫描仪S均值:', round(S_black.mean(),5),'比例:',round(S_white.mean()/S_black.mean(),5))
    print('白扫描仪V均值:', round(V_white.mean(),5), '\t', '黑扫描仪V均值:', round(V_black.mean(),5),'比例:',round(V_white.mean()/V_black.mean(),5))
    print('白扫描仪V均值:', round(eq_white.mean(),5), '\t', '黑扫描仪V均值:', round(eq_black.mean(),5),'比例:',round(eq_white.mean()/eq_black.mean(),5))

    print(url_white)
    print(url_black)



