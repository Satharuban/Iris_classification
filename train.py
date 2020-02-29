import pandas as pd
from keras.models import Sequential


# from keras.layers import Dense, Activation, Dropout
#
# df = pd.read_csv('iris.csv')
#
# x = df.values[0:, 0]  # feature
#
# y = df.values[0:, 4:]  # labels
#
# j = 0  # create a loop to for assign lables to numeric values
# for i in y:
#     if i == 'setosa':
#         y[j, 0] = 0
#
#     elif i == 'versicolor':
#         y[j, 0] = 1
#     else:
#         y[j, 0] = 2
#     j += 1
#
# # nueral network creation
# model = models.Sequential()
#
# model.add(Dense(32, input_shape=(4, 150)))
# model.add(Activation('tanh'))
# model.add(Dropout(0.5))
#
# model.add(Dense(32))
# model.add(Activation('tanh'))
# model.add(Dropout(0.5))
#
# model.add(Dense(3))
# model.add(Activation('softmax'))
# model.add(Dropout(0.5))
#
# model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])
#
# print(model.summary())
