T = int(input())

outputs = [0] * T


def sum_light(B, adj, light):
    done = []
    s = 0
    for i in range(1, len(B)):
        if light[i]:
            if i not in done:
                s += B[i]
                done.append(i)
            for j in adj[i]:
                if j not in done:
                    s += B[j]
                    done.append(j)
    return s


def lowest(B, adj, num=1, light=None):
    if light is None:
        light = [0] * len(B)
    if num == len(B):
        return sum_light(B, adj, light)
    yesl = light.copy()
    yesl[num] = 1
    yes = lowest(B, adj, num + 1, yesl)
    del yesl
    no = lowest(B, adj, num + 1, light)
    return max([yes, no])


for i in range(T):
    V = int(input())
    B = input().split()
    B = [0] + [int(j) for j in B]
    edges = [[] for j in range(V - 1)]
    adj = [[] for j in range(V + 1)]
    for j in range(V - 1):
        xy = input().split()
        x, y = int(xy[0]), int(xy[1])
        edges[j] = [x, y]
        adj[x].append(y)
        adj[y].append(x)

    outputs[i] = lowest(B, adj)

for i in range(T):
    print("Case #%d: %d" % (i + 1, outputs[i]))
