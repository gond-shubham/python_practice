def palindrome(object):
    if object == object[-1::-1]:
       return "the given word is palindrome"
    else:
        return "It's not palindrome"

print(palindrome(input("enter the string:")))