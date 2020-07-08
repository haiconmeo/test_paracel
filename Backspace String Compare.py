class Solution(object):
    def build(self,S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
    def backspaceCompare(self, S, T):
        
        return self.build(S) == self.build(T)
# https://leetcode.com/problems/backspace-string-compare/