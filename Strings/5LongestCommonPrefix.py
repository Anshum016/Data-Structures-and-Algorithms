def LongestCommonPrefix(str):

    res=""

    for i in range(len(str[0])):
        for s in str:
            if i == len(s) or s[i] != str[0][i]:
                return res
        res +=str[0][i]

    return res


str = ["flower","flow","flight"]
print("Our answer is",LongestCommonPrefix(str))