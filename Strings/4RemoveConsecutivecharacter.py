def removeconsecutivecharacter(str):

    if not str:
        return ""
    
    result=[str[0]]

    for i in range(1,len(str)):
        if str[i] != str[i-1]:
            result.append(str[i])

    return  "".join(result)

str="aaabbccdaa"
print("Our answer is",removeconsecutivecharacter(str))      