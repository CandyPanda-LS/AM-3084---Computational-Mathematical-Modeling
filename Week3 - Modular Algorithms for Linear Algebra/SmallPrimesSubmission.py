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

#calculate all the prime numbers where the product of the primes is less than 2*H + 1
def find_primes(H):
    p = 2*H + 1
    primes = []
    for i in range(2, p):
        if is_prime(i):
            primes.append(i)
        if np.prod(primes) > p:
            return primes

#find the bezout coefficients
def bezout(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = bezout(b, a % b)
        return y, x - y * (a // b)

#############################################################
A = store_matrix()
h = hadamard_bound(A)
print('hadamard_bound',h)
p = find_primes(h)
print('primes',p)

#for all elements in the array p, create matrices that are the same size as A and mod them with the prime number and assign it to an array
mod_matrices = []
for i in range(0, len(p)):
    mod_matrices.append(np.mod(A, p[i]))
print('The modulous matrices are:', mod_matrices)

#find the determinents of all the mod matrices
det_mod_matrices = []
for i in range(0, len(mod_matrices)):
    det_mod_matrices.append(round(np.linalg.det(mod_matrices[i])))
print('The determinents of modulous matrices are:', det_mod_matrices)


#implement the chinese remainder theorem
#find the product of all the primes
M = np.prod(p)
#find the product of all the primes divided by each prime
M_mi = []
for i in range(0, len(p)):
    M_mi.append(M / p[i])

print('M is:', M)
print('M_mi is:', M_mi)

#find the bezout coefficients of the product of all the primes divided by each prime and each prime
bezout_coeff = []
for i in range(0, len(p)):
    bezout_coeff.append(bezout(M_mi[i], p[i]))
print('bezout_coeff is:', bezout_coeff)

#find the sum of the determinent of the mod matrix times the bezout coefficient times the product of all the primes divided by each prime
sum = 0
for i in range(0, len(p)):
    sum += det_mod_matrices[i] * bezout_coeff[i][0] * M_mi[i]
print('sum is:', sum)

var = sum % M
#X = var (Mod M)
#find the array of X that satisfies x = var (Mod M)
# 210 x + 152

#write a switch case statement to find the smallest of 3 numbers

if abs(M * 1 + var) < abs(M * 0 + var) and abs(M * 1 + var) < abs(M * -1 + var):
    cal_det_A = M * 1 + var
elif abs(M * 0 + var) < abs(M * 1 + var) and abs(M * 0 + var) < abs(M * -1 + var):
    cal_det_A = M * 0 + var
else:
    cal_det_A = M * -1 + var


print('cal_det_A is:', cal_det_A)
