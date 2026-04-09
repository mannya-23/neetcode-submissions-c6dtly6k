class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max1 = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] 
                max1 = max(max1, profit)
            else: 
            # if price at r is less than price at l,
            # we found a better buying price → update l to r 
                l = r
            r += 1
        
        return max1 
                