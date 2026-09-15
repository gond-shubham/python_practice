import json
while True:
    try:
        file=input("enter the file name:")
        with open(file, "r") as file_obj:
           data=json.load(file_obj)
           print(data)
           break

    except FileNotFoundError:
           print("File does not exist")
    except json.JSONDecodeError:
           print("Invalid JSON data")

