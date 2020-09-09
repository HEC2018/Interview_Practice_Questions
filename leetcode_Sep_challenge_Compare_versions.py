class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        s1 = [int(i) for i in v1]
        s2 = [int(i) for i in v2] # change version string to integer for comparison
        l1 = len(s1)
        l2 = len(s2)
        l = max(l1, l2)
        s1 = s1 + [0 for _ in range(l+1 - l1)]
        s2 = s2 + [0 for _ in range(l+1 - l2)] # extend the length of two version number. Let them have equal length. All undefined revised are 0
        for i in range(l):
            if(s1[i] > s2[i]):
                return 1
            if(s1[i] < s2[i]):
                return -1
        return 0 # Failed to find the greater version, which results in an equal situation.
        #print(s1)
        #print(s2)
        #return -1
        """
        Tese Cases:
        "0.001"
        "1.01"

        "7.5.2.4"
        "7.5.2"
        
        "7.5.2.4"
        "7.5.3"
        
        "7"
        "8.1"
        
        "7.1"
        "8"
        
        "0.1"
        "0.001"
        
        "1.0.0.000.0001"
        "1.0.01.01.2"
        
        "1.0"
        "1"
        """
        """
        Expected results of test cases:
        -1
        1
        -1
        -1
        -1
        0
        -1
        0
        """