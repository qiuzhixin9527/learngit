import keras
import os
from keras.preprocessing.image import ImageDataGenerator
from keras import models
from keras import layers
from keras import optimizers
from keras.layers import Dense
from keras.layers import Convolution2D, MaxPool2D, Dropout,Flatten


base_dir = './images'

train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'val')
test_dir = os.path.join(base_dir, 'test')


def create_model(model):
#     model = models.Sequential()
    model.add(Convolution2D(16, (3,3), padding='same', activation='relu', input_shape=(224,224,3)))
    model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
    model.add(Dropout(0.25))
    
    model.add(Convolution2D(32,(3,3), padding='same', activation='relu'))
    model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
    model.add(Dropout(0.25))
    
    model.add(Convolution2D(32,(3,3), padding='same', activation='relu'))
    model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
    model.add(Dropout(0.25))
    
    model.add(Convolution2D(64,(3,3), padding='same', activation='relu'))
    model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
    model.add(Dropout(0.25))
    
#     model.add(Convolution2D(64,(3,3), padding='same', activation='relu'))
#     model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
#     model.add(Dropout(0.25))
    
    model.add(Convolution2D(128, (3,3), padding='same', activation='relu'))
    model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
    model.add(Dropout(0.25))
    
    model.add(Convolution2D(128,(3,3), padding='same', activation='relu'))
    model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
    model.add(Dropout(0.25))
    
    model.add(Convolution2D(256, (3,3), padding='same', activation='relu'))
    model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
    model.add(Dropout(0.25))

    
    model.add(Flatten())
    
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.25))
    
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.25))
    
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.25))
    
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))
    
    model.add(Dense(2, activation='softmax'))
    model.summary()
    
    model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-7),
              metrics=['accuracy'])
    
    return model

def ready_data(train_dir, validation_dir, test_dir):
    train_datagen = ImageDataGenerator(
        rescale=1./255,
#         rotation_range=40,
#         width_shift_range=0.2,
#         height_shift_range=0.2,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True,
#         fill_mode='nearest'
    )
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(224, 224),
        batch_size=8,
        class_mode='categorical'
    )
    
    test_datagen = ImageDataGenerator(rescale=1./255)
    validation_generator = test_datagen.flow_from_directory(
        validation_dir,
        target_size=(224, 224),
        batch_size=8,
        # batch_size = 5
        class_mode='categorical')
    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(224, 224),
        batch_size=8,
        # batch_size = 5
        class_mode='categorical')
    
    return train_generator,validation_generator,test_generator
    

model = models.Sequential()
model = create_model(model)
train_generator,validation_generator,test_generator = ready_data(train_dir, validation_dir, test_dir)

history = model.fit_generator(
     train_generator,
     steps_per_epoch=50,
     epochs=50,
     validation_data=validation_generator,
     validation_steps=50
)
model.save('1.h5')
    
