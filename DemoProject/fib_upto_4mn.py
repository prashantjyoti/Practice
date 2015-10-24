def fibonacci(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

fib_series_upto_4mn = fibonacci(4000000)

sum = 0
for number in fib_series_upto_4mn:
    if number%2 == 0:
        sum+=number

print (sum)
    
