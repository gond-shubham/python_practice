with open("names.txt", "w") as obj:
    obj.write("Shubham\n")
    obj.write("Nithin\n")
    obj.write("Santhosh\n")
    obj.write("Nandhini\n")



with open("names.txt", "r") as obj:
    data=obj.read()  #It will read the complete file at once.

print(data)
