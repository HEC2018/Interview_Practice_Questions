class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        out = 0
        for i in range(31,-1,-1): # All integers
            out |= 1 << i # Control bound
            cand = set([out & num for num in nums]) # Selected candidates, which have that bound
            tmp = ans | 1<<i 
            for j in cand:
                if tmp^j in cand: # if a^b == c, then a == b^c
                    ans = tmp
                    break
        return ans
    
    # The main idea: Only focus on first few digits.
    """
    Test Cases:
    [3,10,5,25,2,8]
    [0]
    [8,10,2]
    [14,70,53,83,49,91,36,80,92,51,66,70]
    """
    """
    Expected:
    28
    0
    10
    127
    """