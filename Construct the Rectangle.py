class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        a = int(sqrt(area))
        for i in range(a,0,-1):
            if area % i ==0:
                if area/i>i:
                    return [area/i,i]
                else:
                    return [i,area/i]

# https://leetcode.com/problems/construct-the-rectangle/