from Task3 import check_age

age = int(input("Enter your age: "))
try :
    a = check_age(age)
    print(a)
except ValueError as e:
    print(e)
