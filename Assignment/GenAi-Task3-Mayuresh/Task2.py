def factorial(n):
    if n<0:
        return "value can not be negative try with a positive integer"
        
    elif n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)

print(factorial(5))
print(factorial(0))
print(factorial(-3))


