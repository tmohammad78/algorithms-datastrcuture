"""
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Input: s = "loveleetcode"
Output: 2

"""

# my solution
class Solution(object):
    def firstUniqChar(self, s):
        hashMap = {}
        for ch in s:
            if ch in hashMap:
                hashMap[ch] += 1
            else: 
                hashMap[ch] =  1
        result  = 0
        arr = [value for value in hashMap if hashMap[value] == 1]
        if len(arr) ==0:
            return -1
        for index,value in enumerate(s) :
            if value in arr :
                result = index 
                break
                
        return result

# better solution 
class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = collections.Counter(s)        
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1