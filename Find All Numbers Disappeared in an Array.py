class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        d = set(range(1, len(nums)+1))
        return d -set(nums)
        

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/