class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        dem = 0
        for i in nums:
            if i ==0:
                dem+=1
        while 0 in nums:
            nums.remove(0)
        for i in range(dem):
            nums.append(0)
        return nums

# https://leetcode.com/problems/move-zeroes/