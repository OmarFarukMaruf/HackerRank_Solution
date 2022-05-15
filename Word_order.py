from collections import Counter
N = int(input())
l = list()
for i in range(N):
    l.append(input())
x = Counter(l)
print(len(l))
print(*x.values())