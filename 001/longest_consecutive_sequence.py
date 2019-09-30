class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        l = sorted(set(A))
        maxlength = 0
        start = 0
        if A == []:
            []
        if len(A) == 1:
            return 1
        for i in range(1, len(l)):
            if l[i] != l[i-1] + 1:
                length = i - start
                if length > maxlength:
                    maxlength = length
                start = i
        length = i - start + 1
        if length > maxlength:
            maxlength = length
        return maxlength
    
    def longestConsecutive_n_sq(self, A):
        def inrange(start, end, n):
            for i in range(len(start)):
                if start[i] < n < end[i]:
                    return True
            return False
        if A == []:
            return []
        start = [A[0]]
        end = [A[0]]
        
        for i in range(1, len(A)):
            if inrange(start, end, A[i]):
                continue
            startflag = endflag = False
            if A[i] + 1 in start:
                ind = start.index(A[i] + 1)
                start[ind] = A[i]
                startflag = True
            if A[i] - 1 in end:
                ind2 = end.index(A[i] - 1)
                end[ind2] = A[i]
                endflag = True
            if A[i] in start and A[i] in end:
                ind = start.index(A[i])
                ind2 = end.index(A[i])
                if ind == ind2:
                    continue
                start[ind] = start[ind2]
                del start[ind2], end[ind2]
                startflag = endflag = True
            if not startflag and not endflag:
                start.append(A[i])
                end.append(A[i])
                
        l = [[start[i], end[i]] for i in range(len(start))]
        m = max(l, key=lambda x: x[1] - x[0])
        ind = l.index(m)
        return l[ind][1] - l[ind][0] + 1 #list(range(l[ind][0], l[ind][1] + 1))
