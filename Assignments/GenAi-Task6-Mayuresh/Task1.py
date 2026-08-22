try:
    numerator = int(input("Enter a number: "))
    denominator = int(input("Enter a number: "))
    result = numerator/denominator

except ValueError :     # to check the value enter by user is valid
    print("Enter a number")
except ZeroDivisionError:   # division error for zero dividation
    print("Not divisible by zero")
else:   # runs only when no error occours
    print(result)
finally:    # it will run not matter error comes
    print("Operation Complete")


