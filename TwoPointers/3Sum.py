# Link: https://leetcode.com/problems/3sum/description/

"""Problem Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

## Solution: Time Complexity: O(n^2); Space Complexity: O(n)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1; k=len(nums)-1
            while(j<k):
                target=nums[i]+nums[j]+nums[k]
                if (target==0):
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1; k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and nums[k]==nums[k+1]):
                        k-=1
                    
                elif (target<0):
                    j+=1
                else:
                    k-=1
        return result
