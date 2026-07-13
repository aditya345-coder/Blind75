# Link: https://leetcode.com/problems/container-with-most-water/description/

"""Problem Description:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


## Solution: Time Complexity: O(1); Space Complexity: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum_container=0; i=0; j=len(height)-1
        while(i<j):
            container_size=min(height[i],height[j])*(j-i)
            if (height[i]<=height[j]):
                i+=1
            elif height[i]>height[j]:
                j-=1
            
            if (container_size>maximum_container):
                maximum_container=container_size
                
        return maximum_container
