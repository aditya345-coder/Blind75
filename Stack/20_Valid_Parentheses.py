# Link: https://leetcode.com/problems/valid-parentheses/description/

"""Problem Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


## Solution: Time Complexity: O(n); Space Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        string=list(s)
        stack=[]
        if (len(stack)%2!=0):
            return False
        for ele in string:
            if ((len(stack)!=0) and((stack[len(stack)-1]=='(' and ele==')') or 
            (stack[len(stack)-1]=='[' and ele==']') or 
            (stack[len(stack)-1]=='{' and ele=='}'))):
                stack.pop()
            else:
                stack.append(ele)
        return len(stack)==0
