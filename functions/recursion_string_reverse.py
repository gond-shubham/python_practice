def reverse_string(str1,i=1):
    if i == len(str1):
        return  str1[0]
    return str1[-i] + reverse_string(str1, i=i+1)


s = reverse_string("abcdefghijklmnopqrstuvwxyz")
print(s)


def reverse(text):
    if len(text)==0:
        return ''
    return reverse(text[1:])+text[0]