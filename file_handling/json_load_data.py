import json

with open("menu.json", 'r') as file:
    menu=json.load(file)
    print(menu)

    for item in menu:
        print(item)