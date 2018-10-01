import numpy as np
from keras.datasets import mnist
from keras.callbacks import ModelCheckpoint, Callback, EarlyStopping
from keras.utils import np_utils

from testcallback import TestCallback
from cs231nmodel import CS231NModel
import config


def preprocessing(train: np.ndarray):
    return train.astype(np.float32) / 255


def main(config):
    # data loading & preprocessing
    (X_train_orig, Y_train_orig), (X_test_orig, Y_test_orig) = mnist.load_data()
    X_train = X_train_orig.reshape((-1, 28, 28, 1))
    X_train = preprocessing(X_train)
    X_test = X_test_orig.reshape((-1, 28, 28, 1))
    X_test = preprocessing(X_test)
    Y_train = np_utils.to_categorical(Y_train_orig)
    Y_test = np_utils.to_categorical(Y_test_orig)

    print("X_train shape: {}".format(X_train.shape))
    print("Y_train shape: {}".format(Y_train.shape))

    model = CS231NModel(input_shape=config.INPUT_SHAPE, output_class=config.OUTPUT_CLASS)

    model.compile(loss=config.LOSS,
              optimizer=config.OPTIMIZER,
              metrics=config.METRICS)

    checkpoint = ModelCheckpoint(config.CHECKPOINT_FILEPATH, monitor='val_loss', verbose=1)
    earlystop = EarlyStopping()

    evaluate = TestCallback((X_test, Y_test))

    callbacks_list = [
        checkpoint,
        earlystop,
        evaluate,
    ]

    model.fit(X_train, Y_train,
              batch_size=64, epochs=10, verbose=1,
              callbacks=callbacks_list,  validation_split=0.01)

    if config.SAVE_MODEL:
        model.save(config.SAVE_MODEL_FILENAME)
        print("Model saved to file: {}".format(config.SAVE_MODEL_FILENAME))


if __name__ == '__main__':
    main(config.Config)
