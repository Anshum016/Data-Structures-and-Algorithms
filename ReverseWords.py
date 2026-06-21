class Solution:
    def Reverse(self,s):
        words = s.split()
        n = len(words)

        left = 0
        right = n - 1

        while left < right:
            words[left] , words[right] = words[right] , words[left]

            left +=1
            right -=1
        return " ".join(words)    
    
sol = Solution()
s = "the sky is blue"
answer = sol.Reverse(s)    
print(answer)