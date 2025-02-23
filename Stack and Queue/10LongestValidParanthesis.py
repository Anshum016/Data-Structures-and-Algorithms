def LongestValid(exp):
    stack=[]
    stack.append(-1)
    max_len=0
    for i in range(len(exp)):
        
        if exp[i] == '(':
           stack.append(i)
        else:
            stack.pop()

            if not stack:
                stack.append(i)

            current_length = i - stack[-1] 
            if current_length > max_len:
               max_len = current_length
    return max_len

if __name__ == "__main__":
 exp=")()())"
 print(LongestValid(exp))                      