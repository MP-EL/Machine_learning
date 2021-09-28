# exercise 2.1.3
# (requires data structures from ex. 2.2.1)
from Read_Data import *


import matplotlib.pyplot as plt
from scipy.linalg import svd
import numpy as np

import pandas as pd

filename = 'Data/SAHD.csv'
df = pd.read_csv(filename)
raw_data = df.values  
cols = range(0, 10) 

# X = np.empty((90, 8))
# for i, col_id in enumerate(range(3, 11)):
#     X[:, i] = np.asarray(doc.col_values(col_id, 2, 92))

X = df.to_numpy()


#X = raw_data[:, cols]
attributeNames = np.asarray(df.columns[cols])


classLabels = raw_data[:,-1] # -1 takes the last column
classNames = np.unique(classLabels)
classDict = dict(zip(classNames,range(len(classNames))))
y = np.array([classDict[cl] for cl in classLabels])
N, M = X.shape
C = len(classNames)


# Subtract mean value from data
Y = X - np.ones((N,1))*X.mean()

# PCA by computing SVD of Y
U,S,V = svd(Y,full_matrices=False)

# Compute variance explained by principal components
rho = (S*S) / (S*S).sum() 

threshold = 0.95

# Plot variance explained
plt.figure()
plt.plot(range(1,len(rho)+1),rho,'x-')
plt.plot(range(1,len(rho)+1),np.cumsum(rho),'o-')
plt.plot([1,len(rho)],[threshold, threshold],'k--')
plt.title('Variance explained by principal components');
plt.xlabel('Principal component');
plt.ylabel('Variance explained');
plt.legend(['Individual','Cumulative','Threshold'])
plt.grid()
plt.show()

print('Ran Exercise 2.1.3')