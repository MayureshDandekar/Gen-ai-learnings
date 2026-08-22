from Task3 import check_age

try :
    age = int(input("Enter your age: "))
    a = check_age(age)
    print(a)
except ValueError as e:
    print("Enter a valid age")
