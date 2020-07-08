class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums= sorted(nums)
        return nums[-1]*max(nums[0]*nums[1], nums[-2]*nums[-3])

# https://leetcode.com/problems/maximum-product-of-three-numbers/