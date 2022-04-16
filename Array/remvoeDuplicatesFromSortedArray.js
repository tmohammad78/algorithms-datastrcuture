// The question is :
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/


// python solution : https://leetcode.com/accounts/login/?next=/submissions/detail/681464828/
/**
 * @param {number[]} nums
 * @return {number}
 */
 var removeDuplicates = function(nums) {
    const newNums = new Set(nums)
    nums.length = 0
    nums.push(...newNums.values())
    return newNums.size
};