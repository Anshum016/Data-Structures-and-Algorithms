class stack:
    def __init__(self):
        self.values=[]
    def push(self,x):
        self.values.append(x)
    def pop(self):
        front = self.values[-1]
        self.values = self.values[1:]
        return front


def findduplicate(exp):
    stack=[]
    for ch in exp:
        if ch == ')':
            elements_inside=0
            while stack and stack[-1] != '(':
                elements_inside +=1
                stack.pop()

            if elements_inside == 0:
                return True
        else:
            stack.append(ch)

    return False

if __name__ == "__main__":
    exp= "(((a+(b))+(c+d)))"            

    if findduplicate(exp):
        print("Duplicates Found")
    else:  
        print("Duplicates not found")     
     