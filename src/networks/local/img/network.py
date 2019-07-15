from __future__ import print_function
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, BatchNormalization, Dropout, Conv2D, MaxPooling2D, Flatten
from keras import callbacks


def categorical(y_train, y_validation, nb_dense):
    # Convert class vectors to binary class matrices ("one hot encoding")
    print('[INFO] converting class vectors...')
    y_train_spec = keras.utils.to_categorical(y_train, nb_dense)
    y_validation_spec = keras.utils.to_categorical(y_validation, nb_dense)
    return y_train_spec, y_validation_spec


def architecture(x_train, y_train, x_validation, y_validation, nb_dense, saving_name, opt, nb_epoch):
    # CREATION OF THE NEURAL NETWORK
    model = Sequential()

    # (CONV => RELU) * 1 => POOL
    model.add(Conv2D(filters=32, kernel_size=(3, 3), strides=1, padding='valid', activation='relu'))
    model.add(BatchNormalization(axis=-1))
    model.add(MaxPooling2D(pool_size=(3, 3), strides=None, padding='valid', data_format=None))

    # (CONV => RELU) * 1 => POOL
    model.add(Conv2D(filters=64, kernel_size=(3, 3), strides=1, padding='valid', activation='relu'))
    model.add(BatchNormalization(axis=-1))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid', data_format=None))

    # (CONV => RELU) * 1 => POOL
    model.add(Conv2D(filters=128, kernel_size=(3, 3), strides=1, padding='valid', activation='relu'))
    model.add(BatchNormalization(axis=-1))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid', data_format=None))

    # (CONV => RELU) * 1 => POOL
    model.add(Conv2D(filters=256, kernel_size=(3, 3), strides=1, padding='valid', activation='relu'))
    model.add(BatchNormalization(axis=-1))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid', data_format=None))

    # first (and only) set of FC => RELU layers
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation("relu"))
    model.add(BatchNormalization())
    model.add(Dropout(rate=0.5))

    # use a *sigmoid* activation for multi-label classification
    model.add(Dense(nb_dense))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    cb = callbacks.ModelCheckpoint(saving_name + '.h5', save_best_only=True, period=1)

    hist = model.fit(x_train, y_train, validation_data=(x_validation, y_validation), epochs=nb_epoch,
                     batch_size=32, callbacks=[cb])
    loss_and_metrics_pitch = model.evaluate(x_validation, y_validation, batch_size=32)
    print('loss =', loss_and_metrics_pitch[0], 'accuracy =', loss_and_metrics_pitch[1])

    model.summary()
    return model, hist


def plot(hist):
    # summarize history for accuracy
    plt.plot(hist.history['acc'])
    plt.plot(hist.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['pitch train', 'pitch validation'], loc='lower right')
    plt.show()

    # summarize history for loss
    plt.plot(hist.history['loss'])
    plt.plot(hist.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['pitch train', 'pitch validation'], loc='upper right')
    plt.show()
