class solution(object):
    def isprime(self,n):
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

sol = solution()
print(sol.isprime(8))        