class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        len1 = len(J)
        answer = 0
        for i in range(len1) :
           answer += S.count(J[i])
        return answer