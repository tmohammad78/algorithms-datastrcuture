"""
Given a non-empty array of non-negative integers nums, the degree of this array
is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
that has the same degree as nums.

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.


"""
# My Solution
class Solution(object):
    def findDegree(self,hashMap):
        biggest = -1000
        for value in hashMap:
            length = len(hashMap[value])
            if length > biggest:
                biggest = length
        return biggest
    def findShortestSubArray(self, nums):
        hashMap = {}
        diff = 0
        smallest = 50000
        for index,value in enumerate(nums):

            if value in hashMap:
                hashMap[value].append(index)
                continue
            hashMap[value] = [index]
        
        degreeIndex = self.findDegree(hashMap)
        for i in hashMap:
            if len(hashMap[i]) == degreeIndex :
                difference = hashMap[i][-1] - hashMap[i][0]
                if smallest > difference : 
                    smallest = difference
        return smallest + 1 
        """
        :type nums: List[int]
        :rtype: int
        """
        

# better solution is : https://leetcode.com/problems/degree-of-an-array/solution/