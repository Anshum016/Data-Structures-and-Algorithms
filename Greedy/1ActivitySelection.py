def activity(start,end):
    n = len(start)
    activity_count=0
    finish=-1
    for i in range(n):
        if start[i] > finish:
           finish = end[i]
           activity_count +=1

    return activity_count

start= [10, 12, 20]
end=[20, 25, 30]
print(activity(start,end))       
