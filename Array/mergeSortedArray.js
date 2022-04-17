// This is intresting question , 
// we have two array that are sorted , we want merge this two array even keep this sorting
// question link : https://leetcode.com/problems/merge-sorted-array/


var merge = function(nums1, m, nums2, n) {
  let l = m + n - 1 
  let p1 = m - 1
  let p2 = n - 1
  while( p2 >= 0){
    if(p1 >= 0 && nums1[p1] > nums2[p2]){
      nums1[l--] = nums1[p1--]
    }else{
      nums1[l--] = nums2[p2--]
    }
  }
  return nums1
};