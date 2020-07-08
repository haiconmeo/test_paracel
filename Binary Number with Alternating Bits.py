class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nhiphan = bin(n)
        return all(nhiphan[i] != nhiphan[i+1]
                   for i in range(len(nhiphan) - 1))