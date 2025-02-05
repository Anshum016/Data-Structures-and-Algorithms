from collections import Counter
def validanagram(s,t):
    if len(s) != len(t):
       return False
    
    s_dict=Counter(s)
    t_dict=Counter(t)
    
     
    return s_dict == t_dict 
    

s = "anagram"
t = "nagaram"
print("our answer is",validanagram(s,t))    