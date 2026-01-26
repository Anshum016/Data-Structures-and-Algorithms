class solution:
    def Print1toN(self,i):
        if i < 1:
            return
        self.Print1toN(i-1)
        print(i)

sol = solution()
sol.Print1toN(6)