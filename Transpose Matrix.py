class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        hang,cot = len(A),len(A[0])
        
        kq= [[1] * hang for _ in range(cot)]
        for h, hang in enumerate(A):
            for c,val in enumerate(hang):
                kq[c][h]=val
        return kq
        

# https://leetcode.com/problems/transpose-matrix/