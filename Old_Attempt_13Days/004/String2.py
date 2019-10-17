class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        a = ''
        for i in A.lower():
            if i.isalpha():
                a += i
        return int(a == a[::-1])