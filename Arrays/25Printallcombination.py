import itertools
def PrintAllCombination(arr,r):
   combinations = itertools.combinations(arr,r)

   for combo in combinations:
      print(' , '.join(map(str,combo)))
arr=[1,2,3,4]
r=2
print("Our answer is",PrintAllCombination(arr,r))