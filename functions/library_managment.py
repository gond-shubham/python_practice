books = {

    101: {
        "title": "Atomic Habits",
        "author": "James Clear",
        "status": "available"
    },

    102: {
        "title": "Python Basics",
        "author": "John Smith",
        "status": "borrowed"
    },

    103: {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "status": "available"
    },

    104: {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "status": "borrowed"
    },

    105: {
        "title": "Deep Work",
        "author": "Cal Newport",
        "status": "available"
    },

    106: {
        "title": "Think Like a Monk",
        "author": "Jay Shetty",
        "status": "available"
    },

    107: {
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "status": "borrowed"
    },

    108: {
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "status": "available"
    },

    109: {
        "title": "The Psychology of Money",
        "author": "Morgan Housel",
        "status": "borrowed"
    },

    110: {
        "title": "Ikigai",
        "author": "Francesc Miralles",
        "status": "available"
    }
}


students = {

    "Aman": [102, 107],

    "Rahul": [104],

    "Sneha": [109],

    "Priya": [],

    "Arjun": [101],

    "Neha": [103, 105],

    "Kiran": [],

    "Rithika": [108],

    "Manoj": [],

    "Aditi": [110]
}

# In the students dictionary the names should be complete and unique.



def view():
     print("Here you can see the book status")
     while True:
         print("1.To see single book status.")
         print("2.To see all book status.")
         print("3.exit")
         opt=input("select from above options :")
         match opt:
             case "1":
                while True:
                 id = int(input("input the id of book: "))
                 if id in books:
                     print(books[id])
                     print()
                     break
                 else:
                     print(f'there is no such book with this {id}')
                     print("Do you want to search any different id")
                     opt = input("enter yes/no :")
                     if opt == "yes":
                         continue
                     else:
                         break
             case "2":
                 print("Below are the books, which are available")
                 for i in books:
                     if books[i]["status"] == "available":
                         print(books[i])
                         print()
                 print("Below are the books, which are borrowed")
                 for i in books:
                     if books[i]["status"] == "borrowed":
                         print(books[i])
                         print()
             case "3":
                 break
             case "4":
                 print("invalid option")



def borrow(name):
 while True:
  id = int(input("enter the id of book: "))
  if id in books:
    if books[id]["status"] == "available":
        print("the book is available, you can take it.")
        students[name].append(id)
        books[id]["status"] = "borrowed"
        print(f'{name} has borrowed ')
        break
    else:
        print("the book is not available")
        opt = input("do you want to know, who taken the book yes/no :")
        if opt == "yes":
            for i in students:
                if id in students[i]:
                    print(f'{i} has already borrowed the book {id}')

        print("Do you want to search any other book with other id")
        opt1 = input("enter yes/no :")
        if opt1 == "yes":
            continue
        else:
            print("Thankyou for the visit.")
            break
  else:
      print(f'there is no book with {id} id  ')
      print("Do you want to search any other book with other id")
      opt1=input("enter yes/no :")
      if opt1 == "yes":
          continue
      else:
          break


def return_back(name):
    while True:
        id = int(input("enter the id: "))
        if id in books:
            books[id]['status']='available'
            students[name].remove(id)
            print(f'the students {name} returned the book successfully with id {id}')
            print("Do you have any other books to return")
            opt1= input("enter  yes/no: ")
            if opt1 == "yes":
                continue
            else:
                print("Thanks for visiting")
                break
        else:
            print(f'the given id {id} is wrong')
            print("do you have the proper id or do you taken the book from this library or not")
            opt2= input("enter yes/no: ")
            if opt2 == "yes":
                continue
            else:
                break


def add():
    while True:
        id = int(input("enter the id:"))
        if id not in books:
            books[id]={}
            books[id]["author"]= input("enter the author details : ")
            books[id]["title"] = input("enter the title details : ")
            books[id]["status"] = "available"
        print("Do you have any other new books to add")
        opt1= input("enter yes/no:")
        if opt1 == "yes":
            continue
        else:
            break

def remove():
    while True:
        id = int(input("enter the id:"))
        if id in books:
            del books[id]
            print("do you have any other books to remove")
            opt = input("enter yes /no :")
            if opt == "yes":
                 continue
            else:
                 break
        else:
            print(f'there is no book with id {id}')
            print("do you have the proper id of book to remove")
            opt = input("enter yes /no :")
            if opt == "yes":
                continue
            else:
                break


def library_managment():
    print("welcome to the library managment: ")
    name = input("enter your full name: ")
    while True:
        print("below are the options")
        print("1. view")
        print("2. borrow")
        print("3. return_back")
        print("4. add")
        print("5. remove")
        print("6. exit")
        opt= input("select from above options: ")
        match opt:
            case "view":
                view()
            case "borrow":
                borrow(name)
            case "return_back":
                return_back(name)
            case "add":
                print("Are you from the faculty managment")
                opt1 = input("enter yes/no: ")
                if opt1 == "yes":
                    add()
                else:
                    print(f'only faculties are allowed to add or remove the books.')
            case "remove":
                print("Are you from the faculty managment")
                opt1 = input("enter yes/no: ")
                if opt1 == "yes":
                    remove()
                else:
                    print(f'only faculties are allowed to add or remove the books.')
            case "exit":
                break
            case _:
                print(f'the selected option {opt} is not valid.')






library_managment()














