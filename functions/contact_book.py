contacts = {

    "Aman": "9876543210",
    "Rahul": "9123456780",
    "Sneha": "9988776655",
    "Priya": "9012345678",
    "Arjun": "8899776655",
    "Neha": "9871234560",
    "Kiran": "9765432109",
    "Rohit": "9345678123",
    "Anjali": "9988123456",
    "Vikram": "9090909090",

    "Pooja": "9556677889",
    "Suresh": "9445566778",
    "Meena": "9334455667",
    "Kavya": "9223344556",
    "Ajay": "9112233445",
    "Nisha": "9001122334",
    "Deepak": "9898989898",
    "Rithika": "9787878787",
    "Manoj": "9676767676",
    "Aditi": "9565656565"
}

def add(name):
  while True:
    if name not in contacts:
        num = input("enter the number: ")
        contacts[name] = num
        print(f'the contact {name} is added successfully.')
        print()
        print()
        break
    else:
        print("""please select another name..
                !! please avoid duplicate !! """)
        opt = input("""Do you like to continue to add
                        please give in yes or no : """)

        if opt == "yes" :
            name=input("enter the name again: ")
            continue
        else:
            break


def remove(name):
  while True:
    if name in contacts:
        opt = input("Are you sure.. You want to delete :")
        if opt == "yes":
            del contacts[name]
            print(f'the contact {name} deleted successfully')
            print()
            print()
            break

    else:
        print(f'the given {name} is not in contacts.')
        print("Give the correct name.. Do you want to delete again.")
        opt = input("enter in yes or no: ")
        if opt == "yes":
            name = input("enter the name again: ")
            continue
        else:
            break






def view():
   while True:
    print("Please select from below options: ")
    print("1.To see all contact lists")
    print("2. To see a single contact")
    print("3. Exit")
    opt = input("enter :")
    match opt:
        case '1':
            for i in contacts:
                print(f'the number of {i} is {contacts[i]}')
            print()
            print()
        case '2':
            name = input("enter the name of the contact: ")
            if name in contacts:
                print(f'the {name} number is {contacts[name]}')
                print()
                print()
            else:
                print(f'the {name} is not in contacts ')
                print()
                print()
        case '3':
            print("Exiting")
            print()
            print()
            break



def update(name):
        if name in contacts:
            contacts[name]=input("enter the updated number: ")
            print(f'the contact {name} updated successfully')
            print()
            print()
        else:
            print(f'the {name} contact is not availble.')
            opt = input(" Do you like to add the contact: ")
            if opt == "yes":
                add(name)



def contact_book():
  while True:
    print("you are in contact book")
    print("Below are services in the contact_book")
    print("1. add")
    print("2. remove")
    print("3. view")
    print("4. update")
    print("5.exit")
    opt = input("please enter the service :")
    match opt:
        case "add":
            name =input("enter the name: ")
            add(name)
        case "remove":
            name = input("enter the name: ")
            remove(name)
        case "view":
            view()
        case "update":
            name = input("enter the name: ")
            update(name)
        case "exit":
            break
        case _:
            print("wrong option.. choose the proper one.")



contact_book()







