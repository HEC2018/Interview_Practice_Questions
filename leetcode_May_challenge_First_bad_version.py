# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        while isBadVersion(l) != isBadVersion(r) and l + 1 != r :
            m = (l + r) / 2
            if isBadVersion(m) :
                r = m
            else:
                l = m
        return r
        
        