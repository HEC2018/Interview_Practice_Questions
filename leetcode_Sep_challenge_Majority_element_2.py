import collections.Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter()
        for num in nums:
            count[num] += 1 # If exists, then add. Else, add one element, results in 3 elements in counter
            if len(count) == 3: # Need to eliminate somehow, since 3 elements now
                new_count = Counter()
                for elem, freq in count.items(): 
                    if freq != 1:
                        new_count[elem] = freq - 1 # Eliminate unsatisfied ones
                count = new_count  
        cands = Counter(num for num in nums if num in count)    # Check again for eligibility      
        return [num for num in cands if cands[num] > len(nums)/3]
        """
        Test Cases:
        [3,2,3]
        [1,1,1,3,3,2,2,2]
        [4,4,4,1,2,3,4,4,3,3,8,99]
        [1]
        """
        """
        Expected:
        [3]
        [1,2]
        [4]
        [1]
        """