import numpy as np

#method to take a matrix as user input
def store_matrix():
    #ask the user for the size of the matrix
    n = int(input('Enter the size of the matrix: '))
    #create an empty matrix
    A = np.zeros((n, n))
    #ask the user for the elements of the matrix
    for i in range(0, n):
        for j in range(0, n):
            A[i][j] = int(input('Enter the element at position ' + str(i) + ',' + str(j) + ': '))
    return A

# calculate the hadamard's upper bound for a determinant of a matrix
def hadamard_bound(A):
    #find the absolute value of the heighest value in the matrix
    max = np.amax(np.absolute(A))
    #find the degree of the matrix
    n = np.size(A, 0)
    H = n ** (n/2) * max ** n
    return int(H)

#create a function to check if a number is prime
def is_prime(p):
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


#find a prime number that is greater than the two time hadamard's upper bound +1
def find_prime(H):
    #find the next prime number that is greater than 2*H
    p = 2*H + 1
    while True:
        if is_prime(p):
            return p
        p += 1

#take the element wise modulous of a matrix with a prime number
def mod_matrix(A, p):
    return np.mod(A, p)

#find the determinent of a matrix
def det(A):
    return round(np.linalg.det(A))
#find the bezout coefficients
def bezout(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = bezout(b, a % b)
        return y, x - y * (a // b)



# define a 2x2 matrix using np
A = store_matrix()
print('A =', A)
h = hadamard_bound(A)
print('hadamard_bound',h)
p = find_prime(h)
print('prime',p)
det_A_mod = det(mod_matrix(A,p))
print('det(A) mod p =', det_A_mod)
var = det_A_mod % p
print('var =', var)



if abs(p * 1 + var) < abs(p * 0 + var) and abs(p * 1 + var) < abs(p * -1 + var):
    cal_det_A = p * 1 + var
elif abs(p * 0 + var) < abs(p * 1 + var) and abs(p * 0 + var) < abs(p * -1 + var):
    cal_det_A = p * 0 + var
else:
    cal_det_A = p * -1 + var

print('cal_det_A is:', cal_det_A)

