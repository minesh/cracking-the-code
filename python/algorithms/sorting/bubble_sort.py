array = [3,4,6,7,5,8]

def bubbleSort(array):
   endIndex = len(array) - 2
   swapped = True

   while (swapped):
      swapped = False
      for index in range(endIndex):
         if array[index] > array[index+1]:
            temp = array[index]
            array[index] = array[index+1]
            array[index+1] = temp
            swapped = True
            endIndex -= 1

print array
bubbleSort(array)
print array
