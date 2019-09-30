def common_num(l1, l2):
    c = 0
    for i in l1:
        if i in l2:
            c += 1
    return c

T = int(input())

outputs = [0] * T

for i in range(T):
    ns = input().split()
    N, S = int(ns[0]), int(ns[1])
    mentors = [[0] * (N + 1) for j in range(N + 1)]
    employees = [[] for j in range(N + 1)]
    skill = [[] for j in range(S + 1)]
    nonskill = [[] for j in range(S + 1)]
    nums = [0] * (S + 1)
    for j in range(1, N + 1):
        line = input().split()
        nums[i] = int(line[0])
        line = [int(k) for k in line[1:]]
        employees[j] = line.copy()
        for k in line:
            skill[k].append(j)

    for j in range(1, S + 1):
        nonskill[j] = [k for k in range(1, N + 1) if k not in skill[j]]

    out = 0

    for j in range(1, S + 1):
        out += len(skill[j]) * len(nonskill[j])

    for j in range(1, S + 1):
        for k in range(j + 1, S + 1):
            out -= (common_num(skill[j], skill[k]) * common_num(nonskill[j], nonskill[k]))
    outputs[i] = out
    # print(skill)

for i in range(T):
        print("Case #%d: %d" % (i + 1, outputs[i]))


### Online

# def common_num(l1, l2):
#     c = 0
#     for i in l1:
#         if i in l2:
#             c += 1
#     return c
#
#
# T = int(input())
#
# outputs = [0] * T
#
# for i in range(T):
#     ns = input().split()
#     N, S = int(ns[0]), int(ns[1])
#     mentors = [[0] * (N + 1) for j in range(N + 1)]
#     employees = [[] for j in range(N + 1)]
#     skill = [[] for j in range(S + 1)]
#     nonskill = [[] for j in range(S + 1)]
#     nums = [0] * (S + 1)
#     for j in range(1, N + 1):
#         line = input().split()
#         nums[i] = int(line[0])
#         line = [int(k) for k in line[1:]]
#         employees[j] = line.copy()
#         for k in line:
#             skill[k].append(j)
#
#     for j in range(1, S + 1):
#         nonskill[j] = [k for k in range(1, N + 1) if k not in skills]
#
#     out = 0
#
#     for j in range(1, S + 1):
#         out += nums[j] * (S - nums[j])
#
#     for j in range(1, S + 1):
#         for k in range(j + 1, S + 1):
#             out -= (common_num(skill[j], skill[k]) *
#                     common_num(noskill[j], noskill[k]))
#     outputs[i] = out
#
# for i in range(T):
#     print("Case #%d: %d" % (i + 1, outputs[i]))
