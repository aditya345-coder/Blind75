# Link: https://leetcode.com/problems/group-anagrams/description/

"""Problem Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""


## Solution: Time Complexity: O(n)*O(nlogn); Space Complexity: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for ele in strs:
            curr_element=tuple(sorted(tuple(ele)))
            if curr_element in map.keys():
                map[curr_element].append(ele)
            else:
                map[curr_element]=[ele]
        return list(map.values())

## Solution: Time Complexity: O(n^2); Space Complexity: O(n)
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for word in strs:
            count=[0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            lst=tuple(count)
            dic[lst].append(word)
        
        return list(dic.values())
            
