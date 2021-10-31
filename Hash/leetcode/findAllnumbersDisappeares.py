"""
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

"""

class Solution(object):
    def findDisappearedNumbers(self, nums): 
        hashMap ={}
        # myHash = set(0,)
        # for i in range(0,len(nums) + 1):
        #     hashMap[nums[i]] = None
        # result = []
        # for i in range(1,len(nums)):
        #     print(i)
        #     if i in hashMap:
        #         continue
        #     else:
        #         result.append(i)
        # print(hashMap,result)
        # return result
        complete = set()
        for i in range(1,len(nums)+1):
            complete.add(i)
        
        missing = complete - set(nums)
        return list(complete.difference(set(nums)))
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        