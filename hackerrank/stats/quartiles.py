# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
#num_of_ints = sys.stdin.readline()
#nums = [int(i) for i in sys.stdin.readline().split()]
nums = [3, 7, 8, 5, 12, 14, 21, 13]
nums = [7, 15, 36, 39, 40, 41]

nums = sorted(nums)
print nums

def median(arr):
    if (len(arr) % 2 == 0): #even
        mid_left_index = len(arr) / 2 - 1
        mid_right_index = len(arr) / 2
        return (arr[mid_left_index] + arr[mid_right_index]) / 2
    else:
        return arr[len(arr)/2]

q1_end_index = len(nums) / 2
print nums[0:q1_end_index]
q1 = median(nums[0:q1_end_index])
q2 = median(nums)
if (len(nums) % 2 == 0):
   q3_start_index = len(nums) / 2
else:
   q3_start_index = len(nums) / 2 + 1
print nums[q3_start_index:]
q3 = median(nums[q3_start_index:])
print q1, q2, q3

