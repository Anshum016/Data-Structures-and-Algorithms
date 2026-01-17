class solution(object):
    def pattern(self,n):

        revN = 0
        while n>0:
            lastdigit = n % 10
            revN=(revN*10) + lastdigit
            n = n // 10
        return revN

sol = solution()
print(sol.pattern(5668938403))        



