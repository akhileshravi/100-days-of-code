 
class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        s = ''
        if not A:
            return s
        
        bflag = False
        for i in range(len(A[0])):
            for j in A:
                if len(j) <= i:
                    bflag = True
                    break
                if j[i] != A[0][i]:
                    bflag = True
                    break
            if bflag:
                break
            s += A[0][i]
        return s