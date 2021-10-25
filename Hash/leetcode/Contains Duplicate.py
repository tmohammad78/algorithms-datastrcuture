# Given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if every element is distinct.     

# Input: nums = [1,2,3,1]
#Output: true

class Solution(object):
    def containsDuplicate(self, nums):
        hashmap = set()
        result = False
        for i in nums:
            if i in hashmap:
                result = True
            hashmap.add(i)
        return result
        """
        :type nums: List[int]
        :rtype: bool
        """
        