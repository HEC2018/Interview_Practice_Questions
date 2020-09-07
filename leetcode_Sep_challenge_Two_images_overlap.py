class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        # Writing a solution in O(n^4) is very simple, with brute force. We can do partial optimizations for sparse matrices
        # Collapse the 2D matrices into one matrices, and we compare all possible movements that have at least one overlapping
        # Roughly time complexity: O(A*B), where A and B denotes the number of '1's in matrix A and B, respectively.

        l = len(A)
        a = [(i,j) for i in range(l) for j in range(l) if A[i][j] == 1] 
        b = [(i,j) for i in range(l) for j in range(l) if B[i][j] == 1]
        count = collections.defaultdict(int)
        ans = 0
        for i in a:
            for j in b:
                count[(i[0]-j[0], i[1]-j[1])] += 1 # update the number of overlapping for shifting x = i[0]-j[0], y = i[1] - j[1]
                ans = max(ans, count[(i[0]-j[0], i[1]-j[1])])
        return ans

"""
Test Cases:
[[1,1,0],[0,1,0],[0,1,0]]
[[0,0,0],[0,1,1],[0,0,1]]

[[1,1],[1,1]]
[[0,0],[0,0]]

[[1,0],[0,1]]
[[0,1],[1,0]]

"""