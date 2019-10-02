class Solution:
    # @param A : list of integers
    # @return an integer
    def lrafwd(self, A):
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return A[0]
        current = 0
        start = 0
        for i in range(1, n):
            if A[i] < A[current]:
                nexti = i
                break
        else:
            nexti = n
        max_area = A[current] * (nexti - current)
        for i in range(1, n):
            if i == nexti or A[i] > A[current]:
                current = i
                for j in range(current+1, n):
                    if A[j] < A[current]:
                        nexti = j
                        break
                else:
                    nexti = n
                for j in range(current, 0, -1):
                    if A[j-1] < A[current]:
                        start = j
                        break
                else:
                    start = 0
                area = A[current] * (nexti - start)
                if area > max_area:
                    max_area = area
        
        return max_area
    
    def largestRectangleArea(self, A):
        return self.lrafwd(A)