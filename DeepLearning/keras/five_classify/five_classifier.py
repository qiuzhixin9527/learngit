from keras.models import Sequential
from keras.layers import Conv2D,MaxPool2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callback import Tensorboad, ModelCheckpoint
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session

tensorboard = Tensorboard(log_dir='log')
checkpoint = ModelCheckpoint(filepath='models',monitor='val_acc',mode='auto' ,save_best_only='True')

callback_lists = [tensorboard, checkpoint] 

config = tf.ConfigProto()
config.gpu_options.allocator_type = 'BFC' #A "Best-fit with coalescing" algorithm, simplified from a version of dlmalloc.
config.gpu_options.per_process_gpu_memory_fraction = 0.6
config.gpu_options.allow_growth = True
set_session(tf.Session(config=config))


model = Sequential()

model.add(Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3)))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Conv2D(32, (3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(5, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy']
             )


train_datagn = ImageDataGenerator(
                rescale=1./255,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagn.flow_from_directory(
                './re/train1',
                target_size=(150, 150),  # all images will be resized to 150x150
                batch_size=32,
                class_mode='categorical')
validation_generator = test_datagen.flow_from_directory(
        './re/test1',
        target_size=(150, 150),
        batch_size=32,
        class_mode='categorical') 

model.fit_generator(
        train_generator,
        samples_per_epoch=2000,
        nb_epoch=100,
        validation_data=validation_generator,
        nb_val_samples=800,
        callbacks=callback_lists)
# model.save('1.h5')
