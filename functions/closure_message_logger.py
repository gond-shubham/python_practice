def message_logger():
    L = []                # It won't create default parameter, so for every closure a new list object get created
    def inner(message):
        L.append(message)
        return L
    return inner


logger1= message_logger()
logger1("Logged in")
logger1("Validated access")
print(logger1("successfully completed"))

logger2 = message_logger()
logger2("listened classes")
logger2("practiced coding")
print(logger2("topic completed"))






