T = int(input())

outputs = [0] * T

def smallest(n):
    if n < 10:
        return n
    s = str(n)
    mn = int(s[1:])

    for i in range(1, len(s)):
        n1 = int(s[:i] + s[i+1:])
        if n1 < mn:
            mn = n1
    return mn


for i in range(T):
    n = int(input())
    outputs[i] = smallest(n)

for i in outputs:
    print(i)