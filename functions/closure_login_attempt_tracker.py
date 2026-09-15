def outer():
    attempts = 0
    def login():
      while True:
        name= input("enter the id:")
        password = input("enter the password:")
        if name != "gond shubham" or password != "9492":
            nonlocal attempts
            attempts+=1
            print("invalid id or password")
            if attempts>3:
                print("account locked")
                break
            continue
        else:
            if attempts>3:
                print("id and passwords are correct but the account is locked")
                break
            else:
                attempts =0
                print("Logged in successfully")
                break

    return login

x=outer()

x()




