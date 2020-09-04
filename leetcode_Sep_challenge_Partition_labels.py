class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l = len(S)
        last_d = {}
        for i in range(0,l):
            last_d[S[i]] = i # Mark down the last position of each character
        p = 0
        ans = []
        while p < l:
            e = last_d[S[p]] # get the last of position of the first character in the substring
            i = p + 1
            while i < e:
                if last_d[S[i]] > e: # if we found that the last position is not enough, we extend the length of each part
                    e = last_d[S[i]] 
                i += 1
            ans.append(e-p+1) # append the resulf in list
            p = e + 1 # done work for dividing one substring, continue to next one
        return ans