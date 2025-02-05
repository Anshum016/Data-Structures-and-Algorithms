def RemoveDuplicate(String):
    list=[]

    for char in String:
        if char not in list:
            list.append(char)
    st="".join(list)
    return st
S="aaaaaaaaaabbbbcccdddeeefff"
print("Our Answer is",RemoveDuplicate(S))        