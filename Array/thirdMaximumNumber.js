// Given an integer array nums, return the third distinct maximum number in this array.
//  If the third maximum does not exist, return the maximum number.
// https://leetcode.com/problems/third-maximum-number/
/**
 * @param {number[]} nums
 * @return {number}
 */
 var thirdMax = function(nums) {
  const newArr = nums.sort(function(a, b) {
      return b - a ;
  });
  const mapSet = new Map()
  for(let i =0 ; i< newArr.length ; i++){
      if(mapSet.has(newArr[i])){
          mapSet.get(newArr[i]).push(i)
          continue;
      }
      mapSet.set(newArr[i],[i])
  }
  const maxNumber = Array.from(mapSet.keys())[0] 
  const thirdMaxNumber = Array.from(mapSet.keys())[2] 
  
  mapSet.clear()
  
  if(/\d+/g.test(thirdMaxNumber)){
      return thirdMaxNumber
  }
  return maxNumber

};