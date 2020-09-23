class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gas = [gas[i] - cost[i] for i in range(len(gas))] # Calculate difference
        s = 0
        for g in gas: s += g # Sum of all difference
        if s >= 0:
            start = 0
            ans = 0
            for i in range(len(gas)):
                ans += gas[i]
                if ans < 0: # If we found that there is a sum negative, we then come to a new place
                    # Proof: All leading negs are ignored. If index i is the first solution, then gas[i] >= 0, and all possible sub-sums to i - 1, are negative. Then, our algorithm will change start to i when arrives i - 1. 
                    ans = 0
                    start = i + 1
            return start
        else:
            return -1 # Negative sum. Impossible to drive through all places
        """
        Test Cases:
        [1,2,3,4,5]
        [3,4,5,1,2]

        [2,3,4]
        [3,4,3]

        [4,0,0,1]
        [0,-2,-3,0]

        [4,0,0,0]
        [0,-2,-3,0]
        """
        """
        Expected:
        3
        
        -1
        
        0
        
        0
        """