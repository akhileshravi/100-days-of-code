class Solution:
    def goodNumber(self, N: int):
        n = str(N)
        if '3' in n or '4' in n or '7' in n:
            return False
        notin = 0
        for i in '2569':
            if i not in n:
                notin += 1
        if notin == 4:
            return False
        return True
    def rotatedDigits(self, N: int) -> int:
        c = 0
        # return self.goodNumber(6)
        for i in range(1, N+1):
            if self.goodNumber(i):
                c += 1
        return c