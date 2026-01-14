class solution(object):
    def pattern(self,n):
        number=1
        for i in range(1,n+1):
            
            for j in range(i):
                print(number,end=" ")
                number +=1
            print()

sol = solution()
sol.pattern(5)