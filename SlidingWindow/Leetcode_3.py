# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

"""Problem Description:
Given a string s, find the length of the longest substring without duplicate characters.
"""


## Solution: Time Complexity: O(n^3); Space Complexity: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_list=[]; max_count=0
        for i in range(len(s)): # O(n)
            max_list=[s[i]]; count=1
            for j in range(i+1,len(s)): # O(n)
                if (s[j] in max_list): # O(n)
                    break
                max_list.append(s[j])
            max_count=max(max_count, len(max_list))
        
        return max_count

## Solution: Time Complexity: O(n); Space Complexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
