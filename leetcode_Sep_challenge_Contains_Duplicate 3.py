import heapq as hq
from bisect import bisect_left
from sortedcontainers import SortedList 
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        SL = SortedList()
        l = len(SL)
        for i in range(len(nums)):
            if i > k: 
                SL.remove(nums[i-k-1])   
            pos1 = bisect_left(SL, nums[i] - t)
            pos2 = bisect_right(SL, nums[i] + t)
            if pos1 != pos2 and pos1 != SL:
                return True
            SL.add(nums[i])
        
        return False
    
    """
    Test Cases:
    
    [1,2,3,1]
    3
    0
    
    [2,2,3,3]
    0
    0
    
    [1,3,1,2]
    1
    0
    """
    """
    Expected result:
    true
    false
    false
    """    