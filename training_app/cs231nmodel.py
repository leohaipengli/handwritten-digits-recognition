from keras.models import Model, Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input

def CS231NModel(input_shape: tuple, output_class: int):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape, name='conv_1'))
    model.add(Conv2D(64, (3, 3), activation='relu', name='conv_2'))
    model.add(MaxPooling2D(pool_size=(2, 2), padding='same', name='maxpool_1'))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(output_class, activation='softmax'))

    return model

