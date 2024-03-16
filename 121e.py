class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxFoundProfit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l=r
            else:
                moneyMade = prices[r] - prices[l]
                maxFoundProfit = max(maxFoundProfit, moneyMade)
                r+=1

        return maxFoundProfit
