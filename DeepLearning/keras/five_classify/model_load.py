from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator

model = load_model('best_weights.h5')
test_datagn = ImageDataGenerator(rescale=1./255)
test_generator = test_datagn.flow_from_directory(
                 './re/validation1',
                 target_size=(150, 150),
                 batch_size=32,
                 class_mode='categorical')

classer = model.evaluate_generator(test_generator)
print(classer)
