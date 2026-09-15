import json

file=open("restaurant_data.json", 'r')
data=json.load(file)
file.close()

print(data["name"])
location=data["location"]
print(location["city"])
print(location["pincode"])

menu=data["menu"]

for item in menu:
    print(f'{item["name"]}-->{item["price"]}')

