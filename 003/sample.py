from itertools import combinations

def check(left, H, l=[], s=0, done=[]):
    if left == []:
        if s >= H:
            return 1
        else:
            return 0
    if length(left) == 1:
        if s + left[0] >= H:
            return 1
        else:
            return 0
    tot = 0
    for i in range(len(left)):
        if s + left[i] >= H:
            tot += 2 ** (len(left) - i - 1)
        else:
        	tot += check(left[i:], H, l, s, done)
        	tot += check(left[i:], H, l, s, done)
    return tot
def fn(A, B, N, H):
    anum = bnum = 0
    aflag = bflag = True
    # for j in range(N, 0, -1):
    # 	# adone = []
    #     if aflag:
    #         aflag = False
    #         for lst in combinations(A,j):
    #             if sum(lst) >= H:
    #                 aflag = True
    #                 anum += 1
    #                 # print(lst)
    #     if bflag:
    #         bflag = False
    #         for lst in combinations(B,j):
    #             if sum(lst) >= H:
    #                 bflag = True
    #                 bnum += 1
        
    #     if not aflag and not bflag:
    #         break
    anum, bnum = check(A, H), check(B, H)
    return anum,bnum
    
summer = sum
length = len      
        
def main():
    T = int(raw_input())

    summer = sum
    length = len
    outputs = [0]  * T
    for i in range(T):
        nh = raw_input().split()
        N, H = int(nh[0]), int(nh[1])
        A = [int(j) for j in raw_input().split()]
        A.sort()
        B = [int(j) for j in raw_input().split()]
        B.sort()
        outputs[i] = fn(A, B, N, H)
    
    for i in range(T):
        print("Case #%d:" % (i+1), outputs[i])

main()
