class solution():
    def reverseQueue(self,q):
        stack=[]

        while len(q) != 0:
            x = q.pop(0)
            stack.append(x)

        while len(stack) != 0:
            x = stack.pop()
            q.append(x)

        return q
    
q = [1, 2, 3, 4] 
solution1 = solution()
reveredqueue =  solution1.reverseQueue(q)
print(reveredqueue)
