def validpalindrone(str):
    n=len(str)
    l=0
    r=n-1

    while l<r:
        if not str[l].isalnum():
            l+=1
            continue
        if not str[r].isalnum():
            r-=1
            continue
        if str[l].lower() !=str[r].lower():
            return False
        
        l +=1
        r-=1
        return True

str="A man, a plan, a canal: Panama"             
print("Our Answer is",validpalindrone(str))