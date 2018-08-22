import numpy as np
from keras import models
from keras.layers import Flatten, Dense
from keras.layers import Convolution2D, MaxPooling2D, Dropout
from PIL import Image as pil_image


model = models.Sequential()
model.add(Convolution2D(32, (3, 3), padding='same',activation='relu', input_shape=(224, 224, 3)))
model.add(MaxPooling2D(pool_size = (2, 2),strides = (2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(32, (3, 3), padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size = (2, 2),strides = (2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, (3, 3), padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size = (2, 2),strides = (2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, (3, 3), padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size = (2, 2),strides = (2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(128, (3, 3), padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size = (2, 2),strides = (2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(128, (3, 3), padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size = (2, 2),strides = (2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(256, (3, 3), padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size = (2, 2),strides = (2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())


# model.add(layers.Dense(2, activation='softmax'))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.25))

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.25))

model.add(Dense(2, activation='softmax'))
model.summary()

model.load_weights('./weights_cover.h5')

# define glob variable
url = '/home/chenm/Documents/shiqiao/彩色Hp扫描仪/meng01_1.jpg'
new_h, new_w = 224, 224
img = pil_image.open(url)
img = np.asarray(img, dtype=np.float32)
count = 0

for i in range(11):
    top = np.random.randint(4000, 6500)
    left = np.random.randint(500, 4000)
    image_random = img[top: top + new_h,
                       left: left + new_w]
    x = image_random / 255.
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    print(preds)
    print(np.argmax(preds))
    if np.argmax(preds) == 1:
        count += 1
print(count)
