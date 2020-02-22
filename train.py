import pandas as pd

df = pd.read_csv('iris.csv')


x = df.values[0:,0]# feature

y = df.values[0:,4:] #labels


j = 0             #create a loop to for assign lables to numeric values
for i in y:
    if i=='setosa':
        y[j,0]=0

    elif i=='versicolor':
        y[j,0]=1
    else:
        y[j,0]=2
    j+=1


