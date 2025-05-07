def VariableSlidingWindow(str):
    n=len(str)
    longest=0
    sett = set()
    l = 0

    for r in range(n):
        while str[r] in sett:
            sett.remove(str[l])
            l += 1

        window_length = (r-l) + 1 
        longest = max(window_length,longest)
        sett.add(str[r])

    return longest    

str= "abcabcbb"
print(VariableSlidingWindow(str))
