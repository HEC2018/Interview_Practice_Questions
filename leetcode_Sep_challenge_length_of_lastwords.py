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
        # We can revise the solution through just running through the last word but not split.
        """
        Revised:
        class Solution(object):
            def lengthOfLastWord(self, s):
                """
                :type s: str
                :rtype: int
                """
                end = len(s) - 1
                while end > 0 and s[end] == " ":
                    end -= 1
                begin = end
                while begin >= 0 and s[begin] != " ":
                    begin -= 1
                return end - begin
        """