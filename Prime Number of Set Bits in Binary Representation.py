class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(n).count('1') in primes for n in range(L, R+1))



# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/