
e.g. [1,2,3] sumTotal 5
def findSubset(array, subset, sumTotal):
   if (subset and sum(subset) == sumTotal):
      return subset
   else:
      if not subset:
         subset = 
      findSubset(array[0:len(array)-1], array[len(array)-1], sumTotal)



