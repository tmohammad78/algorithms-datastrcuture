"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique  and you may return the result in any order.

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

"""
class Solution(object):
    def intersection(self, nums1, nums2):
        hashMap = set()
        hashMap2 = set()
        for num in nums1:
            hashMap.add(num)
            
        for num in nums2:
            hashMap2.add(num)
        
        arr = [value for value in hashMap if value in hashMap2]
        return arr