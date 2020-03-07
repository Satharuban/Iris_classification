from keras.models import load_model
import numpy as np

model = load_model('test.h5')


x = np.array([[4.5,3.2,1.6,0.4]])

res=model.predict(x)

ans = np.argmax(res)

class_names = ['Iris-setosa','Iris-versicolor','Iris-virginica']
print("Predicated value ",class_names[ans])