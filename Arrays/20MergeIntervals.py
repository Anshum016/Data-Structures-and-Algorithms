def MergeIntervals(Intervals):
    Intervals.sort(key=lambda x:x[0])
    merged=[]

    for interval in Intervals:
       if not merged or merged[-1][1] < interval[0]:
           merged.append(interval)
       else:
            merged[-1][1]=max(merged[-1][1], interval[1])
    return merged

Intervals=[[1,3],[2,4],[6,8],[9,10]]
print("The answer is",MergeIntervals(Intervals))


 
    