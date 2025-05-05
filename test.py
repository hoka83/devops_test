from operator import index
from pydoc import describe

import pandas as pd
import tensorflow as tf
import keras as ks
import numpy as np
from keras_applications.densenet import layers
from sklearn.model_selection import train_test_split

data = pd.read_csv('D:/New folder/Airline_Delay_Cause/Airline_Delay_Cause.csv')
data = data.drop(['carrier', 'carrier_name', 'airport', 'airport_name'], axis=1)
data.dropna(inplace=True)

data['WDCase'] = data['weather_delay'].apply(lambda x: 1 if x > 100 else 0)

X = data.drop(['WDCase'], axis=1)
y = data['WDCase']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=44, shuffle=True)

#X_train.dropna(inplace=True)
#y_train.dropna(inplace=True)
X_train = X_train.to_numpy()
y_train = y_train.to_numpy()

print(np.any(np.isnan(X_train)))  # Should return False

print(np.any(np.isnan(y_train)))

model = ks.models.Sequential([ks.layers.Dense(8, activation='tanh'), ks.layers.Dense(128, activation='sigmoid'),
                              ks.layers.Dense(64, activation='tanh'),
                              ks.layers.Dense(32, activation='tanh'),
                              ks.layers.Dropout(0.2),
                              ks.layers.Dense(1, activation='sigmoid')])

MyOptimizer = tf.keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)

model.compile(loss='binary_crossentropy', optimizer=MyOptimizer, metrics=['accuracy'])

history = model.fit(X_train, y_train,
                    validation_data=(X_test, y_test),
                    epochs=100,
                    batch_size=10000,
                    verbose=1,
                    callbacks=[tf.keras.callbacks.EarlyStopping(
                        patience=10,
                        monitor='val_accuracy',  #"val_loss",
                        restore_best_weights=True)])

print(model.summary())
