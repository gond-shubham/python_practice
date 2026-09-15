import json

def load_data(file_name):
    try:
        with open(file_name, "r") as file_object:
            data= json.load(file_object)
            return data

    except FileNotFoundError:
        print("File does not exist")
        return []
    except json.JSONDecodeError:
        print("Invalid json data")
        return []

file= input("please enter the file name")
file_data=load_data(file)
print(file_data)

