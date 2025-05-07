def PrefixProduct(nums):
    st=0
    end=0
    poi=0
    n=len(nums)
    curr_sum = 0
    max_so_far=0 
    
    for i in range(n):
        curr_sum = curr_sum + nums[i]
        if (max_so_far < curr_sum):
            max_so_far = curr_sum
            st = poi
            end = i
        if (curr_sum < 0):
            curr_sum =0
            poi +=1

    print("Total Sum:     ",max_so_far)
    print("Starting Point:",st)
    print("Ending Point:  ",end)     

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(PrefixProduct(nums))            