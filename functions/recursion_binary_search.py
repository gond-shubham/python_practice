def binary_search(List, value):
    if len(List) ==0:
        return None
    if len(List)==1:
        if value == List[0]:
          return True
        else:
            return False

    m=len(List)//2
    if value<List[m]:
        return binary_search(List[0:m], value)
    return binary_search(List[m:], value)

l=[10,20,30,40, 50, 60, 70, 80, 90]
value= binary_search(l, value=10)
print(value)

