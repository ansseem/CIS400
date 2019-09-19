# Chris Free

import numpy as np
import time
import random

# - Fill in the code below the comment Python and NumPy same as in example.
# - Follow instructions in document.
###################################################################
# Example: Create a zeros vector of size 10 and store variable tmp.
# Python

pythonStartTime = time.time()
#tmp_1 = [0 for i in range(10)]
pythonEndTime = time.time()

# NumPy
numPyStartTime = time.time()
#tmp_2 = np.zeros(10)
numpyEndTime = time.time()

#print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
#print('NumPy time: {0} sec.'.format(numPyEndTime - numPyStartTime))

z_1 = None
z_2 = None
################################################################
# 1. Create a zeros array of size (3,5) and store in variable z.
# Python

pythonStartTime = time.time()
rows, columns = (3, 5)
z_1 = [[0] * columns] * rows
pythonEndTime = time.time()

# NumPy
numpStartTime = time.time()
z_2 = np.zeros((3, 5))
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
#################################################
# 2. Set all the elements in first row of z to 7.
# Python

pythonStartTime = time.time()
z_1[0] = [7] * 5
pythonEndTime = time.time()

# NumPy
numpyStartTime = time.time()
z_2[:1] = 7
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
#####################################################
# 3. Set all the elements in second column of z to 9.
# Python

pythonStartTime = time.time()
for i in range(3):
    z_1[i][1] = [9]
pythonEndTime = time.time()

# NumPy
numpyStartTime = time.time()
z_2[:, 1] = 9
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
#############################################################
# 4. Set the element at (second row, third column) of z to 5.
# Python

pythonStartTime = time.time()
z_1[1][2] = 5
pythonEndTime = time.time()

# NumPy
numpyStartTime = time.time()
z_2[1][2] = 5
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
##############
print("questions 1-4")
print(z_1)
print(z_2)
##############


x_1 = None
x_2 = None
##########################################################################################
# 5. Create a vector of size 50 with values ranging from 50 to 99 and store in variable x.
# Python

pythonStartTime = time.time()
x_1 = [x for x in range(50, 100)]
pythonEndTime = time.time()

# NumPy
numpyStartTime = time.time()
x_2 = np.arange(50, 100, 1)
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
##############
print("question 5")
print(x_1)
print(x_2)
##############


y_1 = None
y_2 = None
##################################################################################
# 6. Create a 4x4 matrix with values ranging from 0 to 15 and store in variable y.
# Python

pythonStartTime = time.time()
i = 0
y_1 = [[0] * 4 for x in range(4)]
for x in range(4):
    for y in range(4):
        y_1[x][y] = i
        i += 1
pythonEndTime = time.time()

# NumPy

numpyStartTime = time.time()
y_2 = np.arange(16).reshape((4, 4))
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
##############
print("question 6")
print(y_1)
print(y_2)
##############


tmp_1 = None
tmp_2 = None
####################################################################################
# 7. Create a 5x5 array with 1 on the border and 0 inside amd store in variable tmp.
# Python

pythonStartTime = time.time()
tmp_1 = [0] * 5
for i in range(5):
    tmp_1[i] = [1] * 5
for i in range(1, 4):
    for j in range(1, 4):
        tmp_1[i][j] = 0
pythonEndTime = time.time()

# NumPy

numpyStartTime = time.time()
tmp_2 = np.ones((5, 5))
tmp_2[1:-1, 1:-1] = 0
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
##############
print("question 7")
print(tmp_1)
print(tmp_2)
##############


a_1 = None;
a_2 = None
b_1 = None;
b_2 = None
c_1 = None;
c_2 = None
#############################################################################################
# 8. Generate a 50x100 array of integer between 0 and 5,000 and store in variable a.
# Python

pythonStartTime = time.time()
i = 0
a_1 = [[0] * 100 for x in range(50)]
for x in range(50):
    for y in range(100):
        a_1[x][y] = i
        i += 1
pythonEndTime = time.time()

# NumPy

numpyStartTime = time.time()
a_2 = np.arange(5000).reshape((50, 100))
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
###############################################################################################
# 9. Generate a 100x200 array of integer between 0 and 20,000 and store in variable b.
# Python

pythonStartTime = time.time()
i = 0
b_1 = [[0] * 200 for x in range(100)]
for x in range(100):
    for y in range(200):
        b_1[x][y] = i
        i += 1
pythonEndTime = time.time()

# NumPy

numpyStartTime = time.time()
b_2 = np.arange(20000).reshape(100, 200)
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
#####################################################################################
# 10. Multiply matrix a and b together (real matrix product) and store to variable c.
# Python
#couldn't get this one to work :(
# NumPy

numpyStartTime = time.time()
c_2 = np.dot(a_2, b_2)
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
d_1 = None;
d_2 = None
################################################################################
# 11. Normalize a 3x3 random matrix ((x-min)/(max-min)) and store to variable d.
# Python
pythonStartTime = time.time()
d_1 = [[random.randint(1, 100) for x in range(3)] for y in range(3)]
d_1Max, d_1Min = max(max(d_1)), min(min(d_1))

for x in range(3):
    for y in range(3):
        d_1[x][y] = (d_1[x][y] - d_1Min) / (d_1Max - d_1Min)

pythonEndTime = time.time()

# NumPy

numpyStartTime = time.time()
d_2 = np.random.randint(100, size=(3, 3))
d_2Max, d_2Min = d_2.max(), d_2.min()
d_2 = (d_2 - d_2Min) / (d_2Max - d_2Min)
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
##########
print("questions 8-11")
print(d_1)
print(d_2)
#########


################################################
# 12. Subtract the mean of each row of matrix a.
# Python

pythonStartTime = time.time()


def meanRow(mat):
    return sum(mat) / len(mat)


for x in range(len(a_1)):
    tmp = meanRow(a_1[x])
    for y in range(len(a_1)):
        a_1[x][y] = a_1[x][y] - tmp

pythonEndTime = time.time()

# NumPy

numpyStartTime = time.time()
tmp = np.mean(a_2, axis=1)
for x in range(len(tmp)):
    a_2[x] = a_2[x] - tmp[x]
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
###################################################
# 13. Subtract the mean of each column of matrix b.
# Python

pythonStartTime = time.time()
for x in range(len(b_1)):
    tmp = meanRow(b_1[x])
    for y in range(len(b_1)):
        b_1[x][y] = b_1[x][y] - tmp
pythonEndTime = time.time()

# NumPy

numpyStartTime = time.time()
tmp = np.mean(b_2, axis=1)
for x in range(len(tmp)):
    b_2[x] = b_2[x] - tmp[x]
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
################
print("questions 12-13")
print(np.sum(a_1 == a_2), "mean of each row of matrix a")
print(np.sum(b_1 == b_2), "mean of each column of matrix b")
################

e_1 = None;
e_2 = None
###################################################################################
# 14. Transpose matrix c, add 5 to all elements in matrix, and store to variable e.
# Python

pythonStartTime = time.time()

pythonEndTime = time.time()

# NumPy

numpyStartTime = time.time()
e_2 = np.transpose(c_2)
e_2 = e_2 + 5
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))
##################
print("Question 14")
print(np.sum(e_1 == e_2))
##################


#####################################################################################
# 15. Reshape matrix e to 1d array, store to variable f, and print shape of f matrix.
# Python
pythonStartTime = time.time()

pythonEndTime = time.time()

# NumPy

numpyStartTime = time.time()
f = np.ravel(e_2)
numpyEndTime = time.time()

print('Python time: {0} sec.'.format(pythonEndTime - pythonStartTime))
print('NumPy time: {0} sec.'.format(numpyEndTime - numPyStartTime))

print(np.shape(f))