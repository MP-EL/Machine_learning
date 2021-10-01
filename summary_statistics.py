from Read_Data1 import *
import numpy as np
import sys
sys.path.append("02450_toolbox/Tools/toolbox_02450")
from similarity import similarity
np.set_printoptions(suppress=True)
np.set_printoptions(linewidth=np.inf)

numrows = len(X)
numcols = len(X[0])

summaryStatistics = np.empty([9, numcols])
#Mean of X
summaryStatistics[0] =  X.mean(axis=0)
#STD of X
summaryStatistics[1] =  X.std(axis=0)
#Median of X
summaryStatistics[2] =  np.median(X,axis=0)
#Range of X
summaryStatistics[3] =  X.max(axis=0)-X.min(axis=0)
#Covariance

# This is no very usable so far:
print(np.cov(summaryStatistics[0][0:2]))
print(np.cov(summaryStatistics[0][1:3]))
print(np.cov(summaryStatistics[0][2:4]))
print(np.cov(summaryStatistics[0][3:5]))
print(np.cov(summaryStatistics[0][4:6]))
print(np.cov(summaryStatistics[0][5:7]))
print(np.cov(summaryStatistics[0][6:8]))

# This is also not super usefull but it uses the built-in function from the similarity script in the toolbox folder.
print(similarity(summaryStatistics[0][0:2], summaryStatistics[0][1:3], 'cos'))


print(summaryStatistics[:])

#Standardized dataset:
#We dont currently use this :)
Y2 = X - np.ones((N, 1))*X.mean(0)
Y2 = Y2*(1/np.std(Y2,0))
