
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        tam=""
        for w in s:
            tam+=w[::-1]+" "
        return tam.rstrip()

# https://leetcode.com/problems/reverse-words-in-a-string-iii/
        
