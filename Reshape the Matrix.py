class Solution(object):
    def matrixReshape(self,nums, r, c):

        if r * c != len(nums) * len(nums[0]):
            return nums
        flatten = sum(nums, [])
        duoi = [flatten[i*c:(i+1)*c] for i in range(r)]
        return duoi
        

# print(matrixReshape([[1,2], [3,4]],1,4))

#https://leetcode.com/problems/reshape-the-matrix/submissions/
