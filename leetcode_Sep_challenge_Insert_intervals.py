class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        l = len(intervals)
        for i in range(l):
            if newInterval[1] < intervals[i][0]:
                intervals.insert(i, newInterval)
                return intervals # Can be exactly inserted into two consecutive without overlapping
            else:
                if newInterval[0] > intervals[i][1]:
                    continue # Skip the current one since too small
                else:
                    intervals[i] = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])] # Extend
                    if i < l - 1:
                        j = i + 1
                        while j < l and intervals[j][0] <= intervals[i][1]: # Consecutively expand the inserted interval. Delete one totally overlapped
                            intervals[i] = [intervals[i][0], max(intervals[i][1], intervals[j][1])]
                            intervals.pop(j)
                            l -= 1
                    return intervals
        intervals.append(newInterval) # Fails to append (greater than all of intervals)
        return intervals
    
    """
    Test Cases:
    [[1,3],[6,9]]
    [2,5]
    [[1,3],[6,9]]
    [4,5]
    [[1,1],[2,3],[6,9]]
    [1,6]
    [[0,0],[2,3],[6,9],[15,15]]
    [1,14]
    []
    [1,1]
    [[1,1]]
    [1,1]
    """
    """
    Expected:
    [[1,5],[6,9]]
    [[1,3],[4,5],[6,9]]
    [[1,9]]
    [[0,0],[1,14],[15,15]]
    [[1,1]]
    [[1,1]]
    """

    """
    Updated Version: 104ms -> 84ms
    Instead of chaning the original list everytime, we can modify the inserted one, which save codes and time.

    """
    """
    def insert2(self, intervals, newInterval):
        """
       # :type intervals: List[List[int]]
       # :type newInterval: List[int]
       # :rtype: List[List[int]]
        """
        l = len(intervals)
        ans = []
        for i in range(l):
            if newInterval[1] < intervals[i][0]:
                return ans + [newInterval] + intervals[i:] # done work. No need to care about later intervals
            else:
                if newInterval[0] > intervals[i][1]:
                    ans.append(intervals[i]) # Still too small. Skip the current one
                else:
                    newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])] # Extend overlapping one
        return ans + [newInterval] # Fails to find one bigger. Append to the last directly 
"""