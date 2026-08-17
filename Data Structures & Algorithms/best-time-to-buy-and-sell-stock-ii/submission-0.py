class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def rec(i, bought):
            if i == len(prices):
                return 0
            res = rec(i + 1, bought)
            if bought:
                res = max(res, prices[i] + rec(i + 1, False))
            else:
                res = max(res, -prices[i] + rec(i + 1, True))
            return res
        return rec(0, False)