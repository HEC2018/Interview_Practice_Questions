class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = s.split()
        if len(a) == 0:
            return 0
        else:
            return len(a[-1])
        """
        Test Cases:
        "Hello World"
        ""
        "a b cd efff   sd "
        "    a    "
        "q"
        "Ac f op"
        "dhsuidhsiuhdsuad"
        """
        
        """
        Expected:
        5
        0
        2
        1
        1
        2
        16
        """