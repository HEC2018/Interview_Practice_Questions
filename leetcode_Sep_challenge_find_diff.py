class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        """
        c = Counter() 
        for i in s:
            c[i] += 1 # count the occurrence
        for i in t:
            if not(i in c) or c[i] == 0:
                return str(i)
            c[i] -= 1 # subtract occurence if find an elem in c
        """
        ans = 0
        for i in t: ans += ord(i) # sum of the ascii value in t
        for i in s: ans -= ord(i) # minus the sum of ascii value in s
        return chr(ans) 
    """
    Test cases:
    "abcd"
    "abcde"
    
    "acbd"
    "adbcc"
    """
    
    """
    Expected:
    "e"
    
    "c"
    """