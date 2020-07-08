class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        kq = 0
        for i in range(1,len(prices)):
            tam =  prices[i]- prices[i-1]
            if tam > 0 :
                kq +=tam
        return kq
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/