from numpy.core.fromnumeric import size
from Read_Data1 import *
import numpy as np
np.set_printoptions(suppress=True)
np.set_printoptions(linewidth=np.inf)

numrows = len(X)
numcols = len(X[0])

summaryStatistics = np.empty([5, numcols])
#Mean of X
summaryStatistics[0] =  X.mean(axis=0)
#STD of X
summaryStatistics[1] =  X.std(axis=0)
#Median of X
summaryStatistics[2] =  np.median(X,axis=0)
#Range of X
summaryStatistics[3] =  X.max(axis=0)-X.min(axis=0)
#Covariance
#summaryStatistics[4] =  np.cov(X,axis=0)
#corrcoef
# summaryStatistics[4] = 
#print(np.corrcoef(X))


print(summaryStatistics[:])