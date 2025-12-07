# Intro to Matrix Multiplication
# A starter for exploring matrix multiplication

# Import the csv module for handling data
import csv

# Makes presenting a table of data easier
from tabulate import tabulate

# The matrix M is encoded as a list of lists
# Recall that the nested lists serve as the rows of the matrix

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1.2, 3]

M = [ row_1, row_2, row_3]

# We'll import the matrix N from a file using the CSV library
# Recall: This reads in the comma separated-values as a list of lists of strings
#                                               Each line is a list

with open("matrix.txt") as f:
  reader = csv.reader(f)
  N = list(reader)

# By default lists have strings as entries, so convert them to floats
for i in range(len(N)):
  for j in range(len (N[i])):
    N[i][j]=float(N[i][j])

row_1 = [3, -4, 0]
row_2 = [-1, -2, 3]

O = [ row_1, row_2]
    

print(tabulate(M))
print("\n")
print(tabulate(N))
print("\n")


# Challenge 1
# Write a function that returns the dimensions of a matrix

# Returns the dimensions of matrix A as a tuple (number of rows, number of columns)
def matrix_dimensions(A):
  num_rows = len(A)
  num_cols = len(A[0])
  return((num_rows,num_cols))


# Challenge 2
# Write a function that determines if two matrices can be multiplied

# Returns True or False
def can_multiply_matrices(A,B):
  if (matrix_dimensions(A)[1] == matrix_dimensions(B)[0]):
    return True
  else:
    return False

# Challenge 3
# Write a function that determines the entry in row i, column j of the matrix product A*B 

# Returns the entry in row i, column j of the matrix product A*B
def matrix_product_entry(A,B,i,j):
  if can_multiply_matrices(A,B):
    entry = 0
    for k in range (matrix_dimensions(A)[1]):
      entry += B[k][j] * A[i][k]
    return entry
  return None


# Challenge 4
# Write a function that multiplies two matrices A and B

# Returns the matrix product

def matrix_product(A,B):
  if not can_multiply_matrices(A,B):
    return None

  # Initialize a new empty list for your row lists
  rows = matrix_dimensions(A)[0]
  cols = matrix_dimensions(B)[1]
  initial_value = 0

  P = [[initial_value for _ in range(cols)] for _ in range(rows)]

  # Use matrix_product_entry!
  for i in range(matrix_dimensions(A)[0]):
    for j in range(matrix_dimensions(B)[1]):
      P[i][j] = matrix_product_entry(A,B,i,j)
  return P

# Challenge 5
# Write a function that transposes a matrix
  
def matrix_transpose(A):
  
  rows, cols = matrix_dimensions(A)
  initial_value = 0

  M = [[initial_value for _ in range(rows)] for _ in range(cols)]

  for i in range(rows):
    for j in range(cols):
      M[j][i] = A[i][j]
  return M

# TEST CASES FOR MATRIX PRODUCT
def test_matrix_product():
    print("=== Testing matrix_product ===")

    # Test 1: (2x2)*(2x2)
    A = [
        [1, 2],
        [3, 4]
    ]
    B = [
        [5, 6],
        [7, 8]
    ]
    expected_1 = [
        [19, 22],
        [43, 50]
    ]
    print("Test 1 (2x2):", "PASS" if matrix_product(A, B) == expected_1 else "FAIL")

    # Test 2:(2x3)*(3x2)
    A = [
        [2, 0, 1],
        [-1, 3, 2]
    ]
    B = [
        [1, 2],
        [0, 1],
        [4, -1]
    ]
    expected_2 = [
        [6, 3],
        [7, -1]
    ]
    print("Test 2 (2x3 * 3x2):", "PASS" if matrix_product(A, B) == expected_2 else "FAIL")

    # Test 3: Multiply by identity
    I = [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]
    X = [
        [4,5,6],
        [1,2,3],
        [-1,0,2]
    ]
    expected_3 = X
    print("Test 3 (Identity):", "PASS" if matrix_product(I, X) == expected_3 else "FAIL")


# TEST CASES FOR TRANSPOSE
def test_transpose():
    print("\n=== Testing matrix_transpose ===")

    # Test 1: 2x2
    A = [
        [1,2],
        [3,4]
    ]
    expected_1 = [
        [1,3],
        [2,4]
    ]
    print("Test 1 (2x2):", "PASS" if matrix_transpose(A) == expected_1 else "FAIL")

    # Test 2: 2x3 -> 3x2
    A = [
        [5, 7, 9],
        [1, 3, 2]
    ]
    expected_2 = [
        [5, 1],
        [7, 3],
        [9, 2]
    ]
    print("Test 2 (2x3):", "PASS" if matrix_transpose(A) == expected_2 else "FAIL")

    # Test 3: Column vector
    A = [
        [10],
        [20],
        [30]
    ]
    expected_3 = [
        [10, 20, 30]
    ]
    print("Test 3 (3x1):", "PASS" if matrix_transpose(A) == expected_3 else "FAIL")


# RUN ALL TESTS
test_matrix_product()
test_transpose()