class solution(object):
    def is_subsequence(self, s,t):
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i +=1
            j +=1
        if len(s) == i:
            return True
        else:
            return False   

sol = solution()
s = "abc" 
t = "ahbgdc"
answer = sol.is_subsequence(s,t)
print(answer)             
