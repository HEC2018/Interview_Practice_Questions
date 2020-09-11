from sys import maxint
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if len(nums) == 0:
        #   return 0
        ans = -maxint # minimum required
        cur_max = 0
        for num in nums:
            cur_max = cur_max + num # Add up
            if cur_max < 0: cur_max = 0 # If we observe that the sum less than 0, we drop it
            ans = max(cur_max, ans)
        return ans if ans else max(nums) # In case no positive sum, find the maximum in array 
    
    """
    Test Cases:
    [-2,1,-3,4,-1,2,1,-5,4]
    [-2]
    [-2,0,-3]
    [-2,-3]
    [1,2,-5,4]
    [0]
    """
    """
    Expected:     
    6
    -2
    0
    -2
    4
    0
    """