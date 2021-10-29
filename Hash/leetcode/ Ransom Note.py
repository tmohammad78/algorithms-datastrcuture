"""
Given two stings ransomNote and magazine, return true if ransomNote can be constructed
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Input: ransomNote = "aa", magazine = "aab"
Output: true

"""
# my answer 
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hashMap = {}
        result = True
        for ch in magazine:
            if ch in hashMap:
                hashMap[ch] += 1
            else: 
                hashMap[ch] =  1
        for i in ransomNote:
            if i in hashMap and hashMap[i] > 0:
                hashMap[i] -= 1
            else:
                result = False
        return result
            
        

# better answer 
import collections
def canConstruct(self, ransomNote, magazine):
    return not collections.Counter(ransomNote) - collections.Counter(magazine)