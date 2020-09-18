class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l < 2:
            return 0 # Impossible to make a valid transaction
        ans = 0
        mi = prices[0] # Starting price
        for i in range(1, l):
            ans = max(ans, prices[i] - mi) # Update the profit
            mi = min(mi, prices[i]) # Update minimum price
        return ans
    """
    Test Cases:
    [7,1,5,3,6,4]
    [7,6,4,3,1]
    [8,10,3,20,1]
    []
    [0,1]
    [2]
    [4995,290,109,109,1903,1090,109000]
    """
    """
    Expected:
    5
    0
    17
    0
    1
    0
    108891
    """