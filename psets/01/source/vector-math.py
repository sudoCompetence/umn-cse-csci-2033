import numpy as np
# from numpy import linalg as LA


# print definitions
def print_vectors(v1, v2):
    print("Vector One \n {}".format(v1))
    print("Vector Two \n {}".format(v2))


def print_vector_add(v1, v2, v1Add2):
    print("VectorOne + VectorTwo \n")
    print("{} + {} = [{}".format(v1[0], v2[0], v1Add2[0]))
    print("{} + {} =  {}".format(v1[1], v2[1], v1Add2[1]))
    print("{} + {} =  {}]".format(v1[2], v2[2], v1Add2[2]))
    print("Resultant vector \n {}".format(v1Add2))


def print_vector_mult(v1, v2, v1Mult2):
    print("VectorOne x VectorTwo \n")
    print("{} x {} = [{}".format(v1[0], v2[0], v1Mult2[0]))
    print("{} x {} =  {}".format(v1[1], v2[1], v1Mult2[1]))
    print("{} x {} =  {}]".format(v1[2], v2[2], v1Mult2[2]))
    print("Resultant vector \n {}".format(v1Mult2))


def print_vector_math(n, v1, k, v2, vectorMath):
    print("({})(VectorOne) * ({})(VectorTwo)\n".format(n, k))
    print("Scalars")
    print("({})*{} = {}".format(n, v1[0], n*v1[0]))
    print("({})*{} = {}".format(n, v1[1], n*v1[1]))
    print("({})*{} = {}".format(n, v1[2], n*v1[2]))
    print("({})*{} = {}".format(k, v2[0], k*v2[0]))
    print("({})*{} = {}".format(k, v2[1], k*v2[1]))
    print("({})*{} = {}".format(k, v2[2], k*v2[2]))
    print("Results")
    print("[{} + {} = {}".format(n*v1[0], k*v2[0], vectorMath[0]))
    print(" {} + {} = {}".format(n*v1[1], k*v2[1], vectorMath[1]))
    print(" {} + {} = {}]".format(n*v1[2], k*v2[2], vectorMath[2]))


def print_vector_dot(v1, v2, vf):
    v1v2r1 = v1[0]*v2[0]
    v1v2r2 = v1[1]*v2[1]
    v1v2r3 = v1[2]*v2[2]
    print("VectorOne X VectorTwo \n")
    print("{} x {} = {} \n".format(v1[0], v2[0], v1v2r1))
    print("{} x {} = {} \n".format(v1[1], v2[1], v1v2r2))
    print("{} x {} = {} \n".format(v1[2], v2[2], v1v2r3))
    print("Results")
    print("[{} + {} + {} = {}".format(v1v2r1, v1v2r2, v1v2r3, vf))


def print_vector_norm(v1, vf, norm):
    v1r1r1 = v1[0]*v1[0]
    v1r2r2 = v1[1]*v1[1]
    v1r3r3 = v1[2]*v1[2]
    print("VectorOne X VectorTwo \n")
    print("{} x {} = {} \n".format(v1[0], v1[0], v1r1r1))
    print("{} x {} = {} \n".format(v1[1], v1[1], v1r2r2))
    print("{} x {} = {} \n".format(v1[2], v1[2], v1r3r3))
    print("Dot Product (inner)")
    v1Dot1 = v1r1r1 + v1r2r2 + v1r3r3
    print("{} + {} + {} = {} \n".format(v1r1r1, v1r2r2, v1r3r3, v1Dot1))
    print("Norm")
    print("sqrt{} = {} \n".format(v1Dot1, norm))


# print bools
printVectorOne = False
printVectorMath = True
printVectorAdd = False
printVectorMult = False
printVectorDot = False
printVectorNorm = False

# define vectors
s1 = 2
s2 = -1
v1 = np.array([[1], [2], [3]])
v2 = np.array([[4], [5], [6]])
v1 = np.array([[1], [2], [3]])
v2 = np.array([[1], [5], [-1]])

# math
v1Add2 = v1 + v2
v1Mult2 = v1 * v2
vectorMath = (s1*v1) + (s2*v2)

# dot product; must flatten vector before product (inner)
v2f = v2.flatten()
v1f = v1.flatten()
v1Dot2 = np.inner(v1f, v2f)

# norm (absolute magnitude of vector)
v1Dot1 = np.inner(v1f, v1f)
v1Norm = np.sqrt(v1Dot1)


# print conditions
if printVectorOne:
    print_vector_math
    print_vectors(v1, v2)

if printVectorAdd:
    print_vector_add(v1, v2, v1Add2)

if printVectorMult:
    print_vector_mult(v1, v2, v1Mult2)

if printVectorMath:
    print_vector_math(s1, v1, s2, v2, vectorMath)

if printVectorDot:
    print_vector_dot(v1, v2, v1Dot2)

if printVectorNorm:
    print_vector_norm(v1, v2f, v1Norm)
