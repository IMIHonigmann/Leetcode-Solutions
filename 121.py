class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxFoundProfit = 0

        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l+=1
            else:
                if prices[r] - prices[l] > maxFoundProfit:
                    maxFoundProfit = prices[r] - prices[l]
                r+=1

        return maxFoundProfit
