class Solution(object):
    def anagram(self,s,t):
        s_freq= {}
        t_freq= {}

        for i in s:
            s_freq[i] = s_freq.get(i,0) + 1
        for j in t:
            t_freq[j] = t_freq.get(j,0) + 1
 
        if s_freq == t_freq:
            return True
        else:
            return False


sol = Solution()
s = "anagram"
t = "nagaram"
answer = sol.anagram(s,t)
print(answer)