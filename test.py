#import pandas as pd

#mydata = pd.read_csv("http://www-stat.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data")
#print(mydata)

def f(x):
    def g(y):
        x+y
    return g

a = f(5)
b = a(5)
print(b)


