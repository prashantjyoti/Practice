__author__ = 'prashant_jyoti'

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

def nthPrimeNumber(limit):
    answer, count = 0,1
    for i in range(3,200000,2):
        if(isPrime(i)):
            count += 1
            if(count == limit):
                answer = i
                break
            else:
                continue
    return answer


limit = input("enter limit: ")
answer = nthPrimeNumber(int(limit))
print (answer)



