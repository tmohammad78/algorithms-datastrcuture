"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Input: nums = [1,2,3,1], k = 3
Output: true

Input: nums = [1,0,1,1], k = 1
Output: true
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashMap = {}
        result= False
        for index,item in enumerate(nums):
            if item in hashMap:
                hashMap[item].append(index)
                if abs(hashMap[item][-2] - hashMap[item][-1]) <= k:
                    result = True
                continue
            hashMap[item] = [index]

        return result