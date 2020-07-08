class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack  = []
        dic = {
            ')' :'(',
            '}' : '{',
            ']' : '['
        }
        for ch in s:
            if ch in dic:
                top  =  stack.pop() if stack else '#'
                
                if dic[ch]!= top:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0
# https://leetcode.com/problems/valid-parentheses/