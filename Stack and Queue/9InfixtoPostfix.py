def prec(c):
    if c == '^':
        return 3
    elif c == '*' or c == '/':
        return 2
    elif c == '-' or c == '+':
        return 1
    else:
        return -1

def infixtopostifx(exp):
    stack=[]
    result=""

    for c in exp:
        # if there is an operand add it to result
        if c.isalnum():
            result +=c
        # if there is ( then add normally to stack    
        elif c == '(':
            stack.append(c)
        # if there is ) then pop all elements from stack until and unless you do not get ( and then also remove (    
        elif c == ')':
            while stack[-1] != '(':
                result +=stack.pop()
            stack.pop()
        # Now if the precedence of the current operator that are we going to add in the stack is less than that of the top element of the stack then pop all elements from stack and add to the result     
        else:
            while stack and (prec(c) <= prec(stack[-1]) ):
              result +=stack.pop()
            stack.append(c)
        #Now remove the remaining elements and add it to result    
    while stack:       
        result += stack.pop()
    print(result) 

exp = "a+b*(c^d-e)^(f+g*h)-i"
infixtopostifx(exp)


                
   
