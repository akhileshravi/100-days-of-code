def diff(A):
    s = 0
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            s += 1
    return s

def left(A, k, ind=1, changed=0, truth = True):
    if diff(A) <= k:
        return changed
    if ind != len(A):
        if A[ind] != A[ind-1]:
            A1 = A.copy()
            A1[ind] = A1[ind] - 1
            yes = left(A1, k, ind+1, changed+1, truth)
            no = left(A, k, ind+1, changed, truth)
            if yes == -1:
                return no
            if no == -1:
                return yes
            return min([yes, no])
        return left(A, k, ind+1, changed, truth)
    else:
        return -1

T = int(input())

outputs = [0] * T

for i in range(T):
    nk = input().split()
    N, K = int(nk[0]), int(nk[1])
    A = input().split()
    A = [int(j) for j in A]
    m = min([left(A, K), left(A[::-1], K)])
    outputs[i] = m

for i in range(T):
        print("Case #%d: %d" % (i + 1, outputs[i]))
