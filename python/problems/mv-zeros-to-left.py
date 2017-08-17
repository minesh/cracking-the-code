#!/usr/bin/env python

def moveZerosLeft(array):
   ptr = 0
   for index, item in enumerate(array[1:], 1):
      if item == 0:
         array[ptr], array[index] = array[index], array[ptr]
         ptr += 1

testArray = [0, 1, 1, 0, 1, 0 , 0]
moveZerosLeft(testArray)
print testArray

