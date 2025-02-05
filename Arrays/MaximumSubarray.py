def maximum_sub_array(arr):
    size=len(arr)
    curr_sum=0
    max_so_far=arr[0]
    st=0;end=0;poi=0

    for i in range(0,size):

        curr_sum = curr_sum+arr[i]
        if (max_so_far < curr_sum):
         max_so_far = curr_sum
         st=poi 
         end=i

        if (curr_sum < 0):
            curr_sum = 0 
            poi = i+1
    print("Maximum sub array is" , max_so_far)
    print("Start index of window" , st)
    print("Closing index of window", end)

arr=[-2,1,-3,4,-1,2,1,-5,4]
maximum_sub_array(arr)