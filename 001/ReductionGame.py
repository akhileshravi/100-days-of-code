T = int(input())
outputs = [0] * T
for i in range(T):
	nk = input().split()
	n, k = int(nk[0]), int(nk[1])
	a = [int(j) for j in input().split()]
	a1 = [j for j in a if j > k]
	a0 = [j for j in a if j not in a1]
	if a1 == []:
		outputs[i] = sum(a)
		continue
	mx = max(a1)
	a1.remove(mx)
	newsum = sum(a1)
	newmax = max(a1)
	if newmax <= newsum//2:
		if newsum % 2 == 0:
			outputs[i] = sum(a0) + k * len(a1) + mx
		else:
			outputs[i] = sum(a0) + k * len(a1) + mx - 1
	else:
		outputs[i] = sum(a0) + k * len(a1) + mx - (2 * newmax - newsum)

