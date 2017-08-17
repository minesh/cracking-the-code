
def maxValue(items):
   
   if (len(items) == 1):
      return items[0]
   max1 = items[0]
   max2 = maxValue(items[1:])

   if (max1 > max2):
      return max1
   else:
      return max2



print maxValue([1,2,3, 6, 2, 1, 0])
