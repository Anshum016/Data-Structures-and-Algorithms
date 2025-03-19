def SmallestNumber(s,d):

    if s == 0 and d == 1:
        return 0
    if s < 1 or s > 9*d:
        return -1
    result=[0] * d
    s -=1  
    for i in range(d-1,0,-1):
        if s > 9:
            result[i] = 9
            s -=9
        else:
            result[i] = s
            s = 0
    result[0] = s + 1
    return int("".join(map(str,result)))

answer = SmallestNumber(9,2)
print(answer)               