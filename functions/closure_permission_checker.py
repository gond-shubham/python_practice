def permission_checker(role):
    def inner(action):
        if role == "admin":
            if action in ["view", "edit", "delete"]:
                return True
            else:
                return False
        elif role == "user":
            if action in ["view", "edit"]:
                return True
            else:
                return False
        else:
            if action in ["view"]:
                return True
            else:
                return False
    return inner



checker_admin= permission_checker("admin") # this closure function remembers the role as admin
checker_user= permission_checker("user") # this closure function remembers the role as user
checker_guest= permission_checker("guest")# this closure function remembers the role as guest

x=checker_user("delete")
print(x)

