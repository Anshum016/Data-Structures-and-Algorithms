def RepeatMissing(arr):
    n=len(arr)
    sum_actual=0
    sum_sq_actual=0

    for num in arr:
        sum_actual +=num
        sum_sq_actual +=num*num
    
    #Ideal sum 
    sum_ideal= n * (n+1) // 2
    sum_sq_ideal = n * (n+1) * (2*n+1) // 6

    #A-B 
    diff = sum_actual - sum_ideal

    #A^2-B^2
    sq_diff = sum_sq_actual - sum_sq_ideal

    #A+B=(A^2-B^2)//(A-B)
    sum_ab = sq_diff // diff

    #Solving A=(A-B + A+B) / 2
    A=(diff + sum_ab) // 2

    #B=A-(A-B)
    B=A-diff

    return [A,B]


arr=[3 ,1, 2, 5, 3]
print(RepeatMissing(arr))
 
