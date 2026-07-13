# Link: https://leetcode.com/problems/valid-palindrome/description/

"""Problem Description:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


## Solution: Time Complexity: O(n^2); Space Complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for i in range(len(s)):
            if (s[i].isalnum()):
                string+=s[i].lower()
        i=0; j=len(string)-1
        while(i<j):
            if string[i]!=string[j]:
                return False
            i+=1; j-=1
        return True

## Solution: Time Complexity: O(n); Space Complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0; right=len(s)-1

        while(left<right):
            while (left<right and not s[left].isalnum()):
                left+=1
            while (left<right and not s[right].isalnum()):
                right-=1
            
            if (s[left].lower()!=s[right].lower()):
                return False
            
            left+=1; right-=1
            
        return True
        
