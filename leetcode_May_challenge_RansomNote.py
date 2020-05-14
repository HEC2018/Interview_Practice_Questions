class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        len1 = len(ransomNote)
        for i in range(len1) :
            if ransomNote.count(ransomNote[i]) > magazine.count(ransomNote[i]) :
                return 0
        return 1
        