#121 ac

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        dp = [0]
        sz = len(prices)
        if sz == 0:
            return 0
        curMin = prices[0]
        for j in range(1,sz):
            if dp[j-1] == 0:
                d = max(0,prices[j]-prices[j-1])
            else:
                d = max(dp[j-1] , prices[j] - curMin )
            dp.append(d)
            curMin = min(curMin,prices[j])
        return dp[len(dp)-1]
