from numpy import array
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers.core import Activation, Dropout, Dense
from keras.layers import Flatten, LSTM
from keras.layers import GlobalMaxPooling1D
from keras.models import Model
from keras.layers.embeddings import Embedding
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.layers import Input
from keras.layers.merge import Concatenate
from keras.layers import Bidirectional

import pandas as pd
X = array(X).reshape(20, 1, 1)

model = Sequential()
import numpy as np
import re

import matplotlib.pyplot as plt

X = list()
Y = list()
X = [x+1 for x in range(20)]
Y = [y * 15 for y in X]
model.add(LSTM(50, activation='relu', return_sequences=True, input_shape=(1,1)))
model.add(LSTM(50, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
# print(model.summary())
model.fit(X, Y, epochs=2000, validation_split=0.2, verbose=1, batch_size=5)

test_input = array([30])
test_input = test_input.reshape((1, 1, 1))
test_output = model.predict(test_input, verbose=0)
print(test_output)