filename = input("Enter Name of the file: ")

try: 
    with open(filename, "r") as f:
        # To print first 3 lines of file
        i = 0
        while i<3:
            print(f.readline().strip())
            i+=1
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You don't have permission to access this file.")
finally:
    print("file operation attempted")