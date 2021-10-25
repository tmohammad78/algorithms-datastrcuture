# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# my solution 
class Solution(object):
    def isAnagram(self, s, t):
        hashMap1 = {}
        hashMap2 = {}
        for ch in s:
            if ch in hashMap1:
                hashMap1[ch] += 1
                continue
            hashMap1[ch] = 1
            
        for ch in t:
            if ch in hashMap2:
                hashMap2[ch] += 1
                continue
            hashMap2[ch] = 1
        return hashMap2 == hashMap1
        
# Better solution 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = collections.defaultdict(int)
        for x in s: tracker[x] += 1
        for x in t: tracker[x] -= 1
        return all(x == 0 for x in tracker.values())