def validparenthesis(s):
    stack=[]
    closetoopen = {")":"("  , "}":"{"   ,  "]":"["}
   
    for c in s:
      if c in closetoopen: 
       if stack and stack[-1] == closetoopen[c]:
           stack.pop()
       else:
          return False
      else:
         stack.append(c)
    return True if not stack else False

s="()"
print("Our answer is",validparenthesis(s)  )     