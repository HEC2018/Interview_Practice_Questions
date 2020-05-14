# Leetcode question 1009
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        i = num
        power = 1;
        while i > 1 :
            m = i % 2
            ans += (1 - m) * power
            i >>= 1
            power <<= 1
        return ans