import os, shutil
import keras

train_dir = '/FaceDectect/SSSp/images/Train'
#validation_dir = '/Downloads/tumelo/Validation'
#test_dir = '/Downloads/tumelo/Test'



#BUilding the CNN

from keras import layers
from keras import models
from keras.layers import Dropout
from keras import optimizers

model = models.Sequential()

#1st convolution layer
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 3)))
model.add(layers.MaxPooling2D((2, 2)))

#2nd convolution layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(Dropout(0.5))

#3rd convolution layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
#model.add(Dropout(0.5))

#flatten
model.add(layers.Flatten())

model.add(Dropout(0.5))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))


model.compile( loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


#DATA PREPROCESSING

from keras.preprocessing.image import ImageDataGenerator

# All images will be rescaled by 1./255
train_datagen = ImageDataGenerator(rescale=1. / 255)
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
        # This is the target directory
        train_dir,
        # All images will be resized to 150x150
        target_size=(48, 48),
        batch_size=40,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')

# validation_generator = test_datagen.flow_from_directory(
#        validation_dir,
 #       target_size=(48, 48),
 #       batch_size=40,
 #       class_mode='binary')

for data_batch, labels_batch in train_generator:
    print('Data batch shape:', data_batch.shape)
    print('Labels batch shape:', labels_batch.shape)
    break


history = model.fit_generator(
      train_generator,
      steps_per_epoch=20,
      epochs=5)

model.save('TRAINED_DATA_gray.h5')

print ("Done Training NANBA")

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
#model.save_weights("model.h5")

print("Converted to JSON")