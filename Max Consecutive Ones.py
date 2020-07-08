class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        kq = 0
        dem=0
        for i in nums:
            if i==1:
                dem+=1
            else :
                kq = max(kq,dem)
                dem=0
        return max(kq,dem)

# https://leetcode.com/problems/max-consecutive-ones/