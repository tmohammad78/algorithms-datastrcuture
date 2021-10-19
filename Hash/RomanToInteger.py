# Roman number to integer number , question in the leetcode 
class Solution(object):
    def romanToInt(self, s):
        count = 0
        myDics ={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        exp = {
            "IV" : 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        for key in exp:
            if key in s:
                count += exp[key]
                s= s.replace(key,"")
        for ch in s:
            if ch in myDics:
                count += myDics[ch]
        return count
        

solv = solution()
# input s ="MCMXCIV"
# M = 1000, CM = 900, XC = 90 and IV = 4.
# 1994
solv.romanToInt("MCMXCIV")