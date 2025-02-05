def contains_duplicate(A):
    return len(A) != len(set(A))

A=[1,23,4,1]
print(contains_duplicate(A))