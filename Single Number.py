class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        kq = []
        for i in nums:
            if i not in kq:
                kq.append(i)
            else:
                kq.remove(i)
        return kq.pop()
# https://leetcode.com/problems/single-number/