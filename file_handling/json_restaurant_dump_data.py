import json

data={}
name=input("please enter the name of the restaurant: ")
data["name"]=name

print("Location")
city = input("please enter the city name: ")
pincode= input("plese enter the pincode: ")
data["location"]= {"city": city, "pincode": pincode}

print("Menu list")
menu=[]
n=int(input("how many items you want to add in menu: "))

for _ in range(n):
    name= input("please enter the item name: ")
    price=int(input("please enter the item price: "))
    menu.append({"name": name, "price":price})


data["menu"]= menu

with open("restaurant_data.json", 'w') as file:
    json.dump(data, file, indent=4)
    file.close()





