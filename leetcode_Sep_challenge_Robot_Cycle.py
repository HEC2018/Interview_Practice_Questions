class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        vec = [0,0]
        direction = [[0,1], [-1,0],[0,-1],[1,0]] # counter-clockwisely from North
        d = 0
        for s in instructions:
            if s == "G":
                vec[0], vec[1] = vec[0] + direction[d][0], vec[1] + direction[d][1] # Compute final vector
            else:
                if s == "L":
                    d -= 1
                    d = d % 4
                else:
                    d += 1
                    d = d % 4
        if d != 0 or (vec == [0,0]): # If the final vector is <0>, or it points to a position other than North
            return True
        else:
            return False
        
        """
        Test cases:
        "GGLLGG"
        "GG"
        "GL"
        "GGGLGG"
        """
        
        """
        Expected:
        true
        false
        true
        true
        """