from collections import defaultdict

d = defaultdict(list)

a, b = map(int, input().split())
for i in range(a):
    s = input().rstrip()
    d[s].append(i+1)
for i in range(b):
    s = input().rstrip()
    if s in d: print(' '.join(map(str, d[s])))
    else: print(-1)
