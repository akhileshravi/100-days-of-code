from math import log, ceil

def xorsum(A, k, M):
    s = 0
    for i in A:
        s += i ^ k
        # if s > M:
        #     return False
    if s > M:
        # if k == 100:
        #     print(s)
        return False
    else:
        return True

def fn():
    nm = raw_input().split()
    N, M = int(nm[0]), int(nm[1])
    A = [int(i) for i in raw_input().split()]

    try:
        item = max([M, max(A)])
        klim = log(item, 2)
    except ValueError:
        klim = 0
    klim = int(ceil(klim))
    print "\nklim:",2 ** klim + 1,'\n' 
    # print(A)
    for k in range(2 ** klim + 1, -1, -1):
        # if k == 100:
        #     print(k, xorsum(A, k, M))
        if xorsum(A, k, M):
            return k
    return -1
    

def main():
    T = int(raw_input())
    outputs = [0] * T
    for i in range(T):
        outputs[i] = fn()
    
    for i in range(T):
        print "Case #%d:" % (i+1), outputs[i]


main()