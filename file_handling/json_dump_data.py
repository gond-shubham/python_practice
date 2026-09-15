import json

with open("menu.json", "w") as file:
    menu_list=[]
    n=int(input("no of entries in menu list: "))

    for _ in range(n):
        menu_list.append({"name":input("enter the item name:"),
                          "price": int(input("enter the item price: ")),
                          "category": input("enter the item category: "),
                          "discount": int(input("enter the discount on item: "))})

    json.dump(menu_list, file)
    print("food items success added in the menu list")