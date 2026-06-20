class Solution(object):
    def valid(self, string):
        result = "" 
        for char in string:
            if char.isalnum():
                result += char.lower()

        reversed = result[::-1]
        if result == reversed:
            return True
        else:
            return False


sol = Solution()
answer = sol.valid("A man, a plan, a canal: Panama")
print(answer)