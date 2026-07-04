def addition(a,b):
    return a + b

def substraction(a,b):
    if b>a:
        return b-a
    else:
        return a - b
    
def multiply(a,b):
    return a * b

def division(a,b):
    if a == 0 or b == 0:
        return "Division by zero is not allowed"
    return a / b