# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        hashMap = {}
        count = 0
        for number in nums :
            if number in hashMap:
                hashMap[number]  = hashMap[number] + 1 
            else:
                hashMap[number] = count
            
        return max(hashMap,key=hashMap.get)


# Input: nums = [2,2,1,1,1,2,2]
# Output: 2