#prime factor of a number n

#from math import sqrt
import time
start_time = time.clock()
def isPrime(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3, int(n**0.5)+1, 2):# only odd numbers
        if n%i==0:
            return False    

    return True

def largest_prime_factor(number):
    max = 0
    for num in range(1,int(number/2),2):
        if(isPrime(num)):
            if(number%num == 0):
                max = num
    return max
    
result = 0
number = input("Enter a number: ")
result = largest_prime_factor(int(number))
print (result)

#add the below statement at the point you want to check execn time
print (time.clock() - start_time, "seconds")


