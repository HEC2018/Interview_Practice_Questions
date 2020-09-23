class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        can = nums[0] # Candidate
        occ = 1
        for i in range(1, len(nums)):
            if nums[i] == can: # More appear
                occ += 1
            else:
                occ -= 1 # reduce the number case
                if occ == 0:
                    can = nums[i] # update to the new one
                    occ = 1
        return can
        """
        Test cases:
        [3,2,3]
        [2,2,1,1,1,2,2]
        [5,1,1,1,5,5,5]
        """
        """
        Expected:
        3
        2
        5
        """