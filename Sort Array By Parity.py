class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        chan = []
        le = []
        for i in A:
            if i %2 :
                le.append(i)
            else:
                chan.append(i)
        return chan+le
# https://leetcode.com/problems/sort-array-by-parity/