T = int(input())
outputs = [0] * T
for i in range(T):
	nk = input().split()
	n, k = int(nk[0]), int(nk[1])
	a = [int(j) for j in input().split()]
	a1 = [j for j in a if j > k]
	a0 = [j for j in a if j not in a1]
	if len(a1) == 0:
		outputs[i] = sum(a)
		continue
	if len(a) == 1:
		outputs[i] = a[0]
		continue

	mx = max(a1)
	a1.remove(mx)
	if len(a1) == 0:
		outputs[i] = sum(a)
		continue
	if len(a1) == 1:
		outputs[i] = sum(a) - 2 * (mx - a1[0])
		continue
	if len(a1) == 2:
		if a1[0] == a1[1]:
			outputs[i] = sum(a0) + 2 * k + mx
			continue
	new_extra_sum = sum(a1) - k * len(a1)
	new_extra_max = max(a1) - k
	if new_extra_max <= new_extra_sum//2:
		if new_extra_sum % 2 == 0:
			outputs[i] = sum(a0) + k * len(a1) + mx
		else:
			outputs[i] = sum(a0) + k * len(a1) + mx - 1
	else:
		outputs[i] = sum(a0) + k * len(a1) + mx - (2 * new_extra_max - new_extra_sum)

for i in outputs:
	print(i)
