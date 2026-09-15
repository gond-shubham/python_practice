import json

def save_data(file_name, data):
    try:
        with open(file_name, "w") as file_object:
            json.dump(data, file_object)
            print("Data updated successfully")

    except TypeError as e:
        print(e)
    except OSError as o:
        print(o)



file_name= input('please enter the file name: ')
data={"name": "ramesh", "age": (1,2,4)}
save_data(file_name, data)



