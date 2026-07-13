# Link: https://leetcode.com/problems/contains-duplicate/description/

"""Problem Description:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

## Solution: Time Complexity: O(nlogn); Space Complexity: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if (nums[i]==nums[i+1]):
                return True
        return False
