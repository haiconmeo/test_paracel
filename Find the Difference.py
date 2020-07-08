class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dem_s = dict()
        for c in s:
            dem_s[c] = dem_s.get(c, 0) + 1
        for c in t:
            if not dem_s.get(c, 0):
                return c
            dem_s[c] -= 1

# https://leetcode.com/problems/find-the-difference/