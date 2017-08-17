class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for index, num in enumerate(nums):
            hash_table[num] = index
        
        for num, index in hash_table.iteritems():
            index1 = index
            if (target - num) in hash_table:
                index2 = hash_table[target - num]
                print (index1, index2)
                return [index1, index2]
            
        return None

if __name__ == '__main__':
   solution = Solution()
   results = solution.twoSum([2, 7, 11, 15], 18)
   if results:
      print "Results for 18 are: %s" % results
   else:
      print "No results"
