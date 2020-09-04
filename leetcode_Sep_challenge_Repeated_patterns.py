# This question has a lot of edge test cases. Be careful.
import numpy as np
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l == 1:
            return False
        bound = l
        prime = np.ones(bound+1, dtype = int) 
        prime_l = []
        prime[0] = 0
        prime[1] = 0
        #print(l)
        #print(bound)
        # if we are unable to partition it into x parts, we are unable to partition it into ax parts for a > 1
        for i in range(2,bound+1):
            if prime[i] != 0:
                prime_l.append(i)
                j = 2
                while j*i <= bound:
                    prime[j*i] = 0
                    j += 1
       # create the bound for the possible length of substrings
        prime_l.reverse()
        for i in prime_l:
            if l % i != 0:
                continue
            sl = l / i
            sample = s[0:sl] # get the substring and prepared for the comparison later
            j = sl
            b = True
            while j <= l - sl:
                if s[j:j+sl] != sample:
                    b = False
                    break;
                j += sl
            if b == False :
                continue
            else:
                return True
        return False