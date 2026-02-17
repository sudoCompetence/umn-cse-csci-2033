import numpy as np
# from numpy import linalg as LA


# define vectors
v1 = np.array([[1], [2], [3]])
v2 = np.array([[4], [5], [6]])
m1 = np.array([[1, 2], [3, 4], [5, 6]])

# print bools
printVectorOne = False
printVectorTwo = False
printMatrix = True
printVectorIndexes = True

# NOTE: the arguments are [ [row1], ... , [rowN] ]
if printVectorOne is True:
    print("Vector One\n {}".format(v1))
    print()

# vector two
if printVectorTwo is True:
    print("Vector Two\n {}".format(v2))
    print()

# matrix two
if printMatrix is True:
    print("Vector Example \n {} \n".format(v1))
    print("vs \n")
    print("Matrix Example \n {}".format(m1))
    print()

# index vector
v1r1 = v1[0]
v1r3 = v1[2]
v1FirstThree = v1[:3]
v1LastTwo = v1[-2:]
if printVectorIndexes is True:
    print("Vector One")
    print("1st row: {}".format(v1r1))
    print("3rd row: {}".format(v1r3))
    print("First three elements: \n {}".format(v1FirstThree))
    print("Last two elements: \n {}".format(v1LastTwo))
    print()
