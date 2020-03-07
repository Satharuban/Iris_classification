from keras.models import Sequential
import pandas as pd
from keras.layers import Dense, Activation, Dropout
from keras import utils
df = pd.read_csv('iris.csv')

x = df.values[0:, 0:4]  # feature

y = df.values[0:, 4:]  # labels

j = 0  # create a loop to for assign lables to numeric values
for i in y:
    if i == 'setosa':
        y[j, 0] = 0

    elif i == 'versicolor':
        y[j, 0] = 1
    else:
        y[j, 0] = 2
    j += 1

model = Sequential()

model.add(Dense(32, input_shape=(4,)))
model.add(Activation('tanh'))
model.add(Dropout(0.5))

model.add(Dense(32))
model.add(Activation('tanh'))
model.add(Dropout(0.5))

model.add(Dense(3))
model.add(Activation('softmax'))


y = utils.to_categorical(y, 3)

model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])

print(model.input_shape)
print(model.output_shape)
print(x.shape)
print(y.shape)


model.fit(x,y,epochs=1001)

model.save('test.h5')