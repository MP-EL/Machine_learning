# exercise 2.1.1
import numpy as np
import xlrd


"""
Explanation of variables in dataset SAHD.xls (african heart disease)
chd: Coronary heart disease (bool) 
sbp: Systolic blood pressure (int)
tobacco: tobacco in kg (float)
ldl: ? (float)
adiposity: ? (float)
famhist: Family history of CHD (bool (Present, Absent)) (string)
typea: ? (int)
obesity: ? (float)
alcohol: alcohol consumption in liters (float)
age: age (int)
"""

# Load xls sheet with data
doc = xlrd.open_workbook('Data/SAHD.xls').sheet_by_index(0)
# Extract attribute names (1st row, column 4 to 12)
attributeNames = doc.row_values(0, 1, 10)

# Extract class names to python list,
# then encode with integers (dict)
classLabels = doc.col_values(0, 1, 463)
classNames = sorted(set(classLabels))
classDict = dict(zip(classNames, range(2)))

# Extract vector y, convert to NumPy array
y = np.asarray([classDict[value] for value in classLabels])

# Preallocate memory, then extract excel data to matrix X
X = np.empty((462, 9))
for i, col_id in enumerate(range(1,10)):
    X[:, i] = np.asarray(doc.col_values(col_id, 1, 463))
# Compute values of N, M and C.
N = len(y)
M = len(attributeNames)
C = len(classNames)

print('Ran Exercise 2.1.1')