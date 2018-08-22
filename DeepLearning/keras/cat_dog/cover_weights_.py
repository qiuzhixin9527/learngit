import keras
import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras import models
from keras import layers
from keras import optimizers
from keras.preprocessing import image

import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras import models
from keras import layers
from keras import optimizers
from keras.layers import Flatten, Dense
from keras.layers import Convolution2D, MaxPooling2D, Dropout


print(keras.__version__)

# from keras.applications import VGG16
#
# conv_base = VGG16(weights='imagenet',
#                   include_top=False,
#                   input_shape=(224, 224, 3))
#
# set_trainable = False
# for layer in conv_base.layers:
#     if 'conv_7b' in layer.name:
#         set_trainable = True
#     if set_trainable:
#         layer.trainable = True
#     else:
#         layer.trainable = False
#
# conv_base.summary()



base_dir = './dataset'

train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'val')
test_dir = os.path.join(base_dir, 'test')

datagen = ImageDataGenerator(rescale=1./255)
realpath = 20



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

model.add(layers.Flatten())


# model.add(layers.Dense(2, activation='softmax'))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.25))

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.25))

model.add(Dense(2, activation='softmax'))
model.summary()

print('This is the number of trainable weights '
      'before freezing the conv base:', len(model.trainable_weights))



train_datagen = ImageDataGenerator(
     rescale=1./255,
     rotation_range=40,
     width_shift_range=0.2,
     height_shift_range=0.2,
     shear_range=0.2,
     zoom_range=0.2,
     horizontal_flip=True,
     fill_mode='nearest'
       )

# Note that the validation data should not be augmented!
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        # This is the target directory
        train_dir,
        # All images will be resized to 150x150
        target_size=(224, 224),
        batch_size=16,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
        validation_dir,
        target_size=(224, 224),
        batch_size=16,
        # batch_size = 5
        class_mode='categorical')

test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(224, 224),
        batch_size=16,
        # batch_size = 5
        class_mode='categorical')


model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-5),
              metrics=['accuracy'])

history = model.fit_generator(
     train_generator,
     steps_per_epoch=50,
     epochs=100,
     validation_data=validation_generator,
     validation_steps=50)

model.save('1.h5')

model.load_weights('./weights_new.h5')

classes = model.evaluate_generator(test_generator)


print(classes)

print(model.predict_generator(test_generator))
