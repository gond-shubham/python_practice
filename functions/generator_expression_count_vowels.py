str1=input("enter the string:")
gen_obj=(1 for i in str1 if i in "AEIOUaeiou")


print(sum(gen_obj))