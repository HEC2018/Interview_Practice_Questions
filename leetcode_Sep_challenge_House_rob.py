class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)        
        if l == 0: 
            return 0 # Soecial case
        dp0 = 0
        dp1 = nums[0]  # Init
        for i in range(1,l):
            dp0, dp1 = max(dp1, dp0), dp0 + nums[i] # DP equation: dp0 means does not rob ith, dp1 otherwise
        return max(dp1, dp0) # return final results
        """
        Test Cases:
        [1,2,3,1]
        [2,7,9,3,1]
        [2,1,3,4,8,10]
        [0]
        [1,101]
        []
        [1,2,4,5,9,2]
        """
        """
        Expected:
        4
        12
        16
        0
        101
        0
        14
        """