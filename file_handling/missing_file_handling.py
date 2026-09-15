import json

file=input("enter the file name:")
try:
    with open(file, 'r') as file_obj:
        data=file_obj.read()
        print(data)
except FileNotFoundError:
    print("The file is not exist")