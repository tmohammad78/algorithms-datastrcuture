"""
Given an array nums containing n distinct numbers in the range [0, n],
 return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2
"""

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)