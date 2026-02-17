# # vector addition
#
# import numpy as np
# # from numpy import linalg as LA
#
# # matrix two
# # NOTE: arguments [ [r1c1, r1c2], [r2c1, r2c2], [r3c1, r3c2]]
# matrix = np.array([[1, 2], [3, 4], [5, 6]])
# printMatrix = True
# if printMatrix is True:
#     print("Matrix Example \n {}".format(matrix))
#     print()
#
# # indexing matrix
# mTwoRowOne = matrix[0]
# mTwoRowOneColOne = matrix[[]]
# mTwoRowTwo = matrix[1]
# mTwoRowThree = matrix[2]
# printMatrixIndexes = True
# if printMatrixIndexes is True:
#     print("1st row of MatrixOne: {}".format(mTwoRowOne))
#     print("2nd row of MatrixOne: {}".format(mTwoRowTwo))
#     print("3rd row of MatrixOne: {}".format(mTwoRowThree))

import numpy as np
# from numpy import linalg as LA


# define vectors (kept for comparison, same as your file)
v1 = np.array([[1], [2], [3]])
v2 = np.array([[4], [5], [6]])

# define matrix
m1 = np.array([[1, 2],
               [3, 4],
               [5, 6]])


# print bools
printVectorExample = True
printMatrixOne = False
printMatrixIndexes = True


# NOTE:
# - Vectors in this convention are Nx1 (a column vector)
# - Matrices are given as [ [row1], ... , [rowN] ]
if printVectorExample is True:
    print("Vector Example \n {} \n".format(v1))
    print("vs \n")
    print("Matrix Example \n {}".format(m1))
    print()


# matrix one
if printMatrixOne is True:
    print("Matrix One\n {}".format(m1))
    print()


# index matrix (same idea as your vector indexing section: name slices, then print them)
m1r1 = m1[0]
m1r3 = m1[2]
m1c1 = m1[:, 0]
m1c2 = m1[:, 1]

m1FirstTwoRows = m1[:2]
m1LastTwoRows = m1[-2:]
m1TopLeft2x3 = m1[:3, :2]
m1BottomLeft2x1 = m1[-1:, :2]

if printMatrixIndexes is True:
    print("Matrix One")
    print("1st row: {}".format(m1r1))
    print("3rd row: {} \n".format(m1r3))
    print("1st column: \n {}".format(m1c1))
    print("2nd column: \n {} \n".format(m1c2))
    print("First two rows: \n {}".format(m1FirstTwoRows))
    print("Last two rows: \n {} \n".format(m1LastTwoRows))
    print("Top-left 3x2: \n {}".format(m1TopLeft2x3))
    print("Bottom-left 1x1: \n {}".format(m1BottomLeft2x1))
    print()
