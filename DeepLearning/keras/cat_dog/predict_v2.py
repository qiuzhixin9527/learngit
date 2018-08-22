import keras
import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras import models
from keras import layers
from keras.applications import VGG16
import cv2

conv_base = VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(224, 224, 3))


model = models.Sequential()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(2, activation='softmax'))

model.load_weights('./weights_new.h5')


# image_file = './dataset/test/fake/'
# image_list = os.listdir(image_file)
# for file in image_list:
#
#     image_path = os.path.join(image_file, file)
#     img = image.load_img(image_path, target_size=(224, 224))
#
#     x = image.img_to_array(img)
#     x = x/255.
#     x = np.expand_dims(x, axis=0)
#
#     preds = model.predict(x)
#     print('Predicted:', preds)
#     print(np.argmax(preds))

count = 0
for i in range(11):
    new_h, new_w = 224, 224
    url = '/home/chenm/Documents/shiqiao/彩色Hp扫描仪/meng01_1.jpg'
    image = cv2.imread(url)
    top = np.random.randint(4000, 6500)
    left = np.random.randint(500, 4000)
    image_random = image[top: top + new_h,
                   left: left + new_w]


    x = image_random / 255.
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    print(preds)
    print(np.argmax(preds))
    if np.argmax(preds) == 1:
        count += 1
print(count)
