class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i] > A[i+1]:
                return i
        
# https://leetcode.com/problems/peak-index-in-a-mountain-array/