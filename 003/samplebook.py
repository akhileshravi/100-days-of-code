def fn():
    nmq = raw_input().split()
    N, M, Q = int(nmq[0]), int(nmq[1]), int(nmq[2])
    P = [int(i) for i in raw_input().split()]
    R = [int(i) for i in raw_input().split()]
    s = 0
    for i in range(Q):
         s += N//R[i]
         for j in range(M):
             if P[j] % R[i] == 0:
                 s -= 1
    return s
    
def main():
    T = int(raw_input())
    outputs = [0] * T
    for i in range(T):
        outputs[i] = fn()
    
    for i in range(T):
        print "Case #%d:" % (i+1), outputs[i]

main()