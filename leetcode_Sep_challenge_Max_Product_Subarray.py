from sys import maxint 
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -maxint
        if len(nums) == 0:
            return 0 # in case it is empty
        cur_max, cur_min = 0, 0 #  cur_max is the maximum product including current digit. Similar cur_min 
        for num in nums:
            if num > 0:
                cur_max, cur_min = max(cur_max*num, num), min(cur_min*num, num) # If num > 0
            else:
                cur_max, cur_min = max(cur_min*num, num), min(cur_max*num, num) # If num <= 0
            ans = max(ans, cur_max)
        return ans if ans else max(nums) # In case special case like [-2], the return shall be -2, but not 0

    """
    Test Cases:
    [2,3,-2,4]
    [1,-9,0,2]
    [1,1,-1,2]
    [10]
    [0]
    []
    [11,-32,0,-90,12]
    [-3,-1,-1]
    [-2,0,-3,0,-1]
    """

    """
    Expected results:
    6
    2
    2
    10
    0
    0
    12
    3
    0
    """