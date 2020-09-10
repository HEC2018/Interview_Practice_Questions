class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0
        dict1 = collections.defaultdict(int)
        dict2 = collections.defaultdict(int)
        secret = [int(i) for i in secret]
        guess = [int(i) for i in guess] # modified to integer for convenience
        l = len(secret)
        for i in range(l): 
            if secret[i] != guess[i]:
                dict1[secret[i]] += 1
                dict2[guess[i]]  += 1 # markdown if mismatched, which is potentially a cow
            else: 
                bull += 1

        for i in dict2:
            if i in dict1:
                cow += min(dict2[i] , dict1[i]) # the difference of the number in two dictionaries
        return str(bull) + "A" + str(cow) + "B"
    """
    Test Case:
    "1807"
    "7810"
    "1323"
    "3133"
    "1123"
    "0111"
    """
    
    """
    Expected:
    "1A3B"
    "1A2B"
    "1A1B"
    """