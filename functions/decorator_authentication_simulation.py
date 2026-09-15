def authentication(fun):
    def wrapper(*args):
        if args[0]== "Gond_shubham" and args[1] == "Kondiba@9492":
            fun(*args)
        else:
            print("Access denied")
    return wrapper


@authentication
def del_account(user_name, password):
    print(user_name)
    print(password)
    print("account successfully deleted.")

del_account("Gond_shubham","Kondiba@9492")