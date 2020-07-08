class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        kq =0
        
        
        tam =[s.count(c) for c in set(s)]
        print (tam)
        for i in tam :
             
            if i%2 :
                kq += i-1
            else :
                kq+=i
            
        return kq +1 if kq <len(s) else kq
            
# https://leetcode.com/problems/longest-palindrome/submissions/
            
