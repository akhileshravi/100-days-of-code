T = int(input())

outputs = [0] * T

for i in range(T):
    ns = input().split()
    N, S = int(ns[0]), int(ns[1])
    employees = [[] for j in range(N + 1)]
    for j in range(1, N + 1):
        line = input().split()
        line = [int(k) for k in line[1:]]
        employees[j] = line.copy()

    ment = 0
    for j in range(1, N + 1):
        for k in range(1, N+1):
            if j != k:
                for l in employees[j]:
                    if l not in employees[k]:
                        ment += 1
                        # print(j, k, l, 'break')
                        break
    outputs[i] = ment

for i in range(T):
    print("Case #%d: %d" % (i + 1, outputs[i]))