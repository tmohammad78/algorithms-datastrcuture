## This is a question from leet code , the question is ,
# base an input array , we should find two number that makes the sum as same as target value
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]],i]
            hash[nums[i]] = i 
        return [-1,-1]
        

solv = solution()
# target is 9 
# array is [2,7,11,15]
# order is O(n)
solv.twoSum([2,7,11,15],9)