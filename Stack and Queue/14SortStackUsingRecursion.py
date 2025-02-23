def insertsortedlist(st,element):

    if not st or st[-1] <=element:
        st.append(element)
    else:
        top=st.pop()    
        insertsortedlist(st,element)
        st.append(top)

def sort_stack(st):
  if st:  
    top=st.pop()
    sort_stack(st)
    insertsortedlist(st,top)



stack = [30, -5, 18, 14, -3]
sort_stack(stack)

while stack:
    print(stack.pop(),end=" ")
print()    

