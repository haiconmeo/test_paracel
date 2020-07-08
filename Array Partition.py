class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tam=sorted(nums)[::2]
        
        return sum(tam)
#https://leetcode.com/problems/array-partition-i/submissions/