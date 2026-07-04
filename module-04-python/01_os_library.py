import os

print(os.getcwd())

print(os.listdir())

# print(os.path.join(os.getcwd(), 'test.txt'))
# with open("test.txt", "r") as file:
#     content = file.read()
#     print(content)

test_dir = '01_os_library.py'
# print(os.path.isdir(test_dir)) 

complete_path = os.path.abspath(test_dir)
print(complete_path)