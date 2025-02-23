from collections import deque

def unique(exp):
    queue=deque()
    freq={}
    result=[]

    for ch in exp:
        freq[ch] = freq.get(ch,0) + 1
        queue.append(ch)


        while queue and freq[queue[0]] > 1:
            queue.popleft()

        result.append(queue[0] if queue else -1) 

    return result
      
exp = ["a", "a", "b", "c"]
print(unique(exp))