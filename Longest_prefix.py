class Solution(object):
    def Longest_prefix(self,strs):
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i +=1
        return first[:i]    
    

sol = Solution()
strs = ["flower","flow","flight"]
answer = sol.Longest_prefix(strs)
print(answer)