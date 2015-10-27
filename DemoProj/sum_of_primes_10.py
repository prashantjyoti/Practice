__author__ = 'Prashant'
import time
start_time = time.clock()
from math import sqrt

def isPrime(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3, int(sqrt(n))+1, 2): # only odd numbers
        if n%i==0:
            return False

    return True

def sum_of_primes(limit):
    sum = 5
    for i in range(4,limit+1):
        if(isPrime(i)):
            sum+=i

    return sum


limit = input("enter limit: ")
print (sum_of_primes(int(limit)))


print (time.clock() - start_time, "seconds")
#
# # def sum_of_primes(limit):
# #     sum = 2+3+5+7+9+11+13+17+19+23
# #     for i in range(4,limit+1):
#         #if(isPrime(6i+1)):
#    # sum+=6i+1
#     elif(isPrime(6i-1)):
#     sum+=6i-1
#     else:
#     continue
# #
# #
# #     return sum