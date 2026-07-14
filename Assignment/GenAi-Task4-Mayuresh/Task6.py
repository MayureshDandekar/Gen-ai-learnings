import os

user = input("Enter the file name: ")

if os.path.exists(user):
    with open(user, "r") as file:
        print(file.read())
else:
    print("File not found, PLease heck the filename")
        
    
