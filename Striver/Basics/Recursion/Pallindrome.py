class solution:
    def Pallindrome(self,string,i,n):
        if i >=n//2:
            return True
        if string[i] != string[n-i-1]:
            return False
        return self.Pallindrome(string,i+1,n)
        

sol = solution()
string="helloef"
print(sol.Pallindrome(string,0,len(string)))

