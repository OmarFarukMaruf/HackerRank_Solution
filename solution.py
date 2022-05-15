n=int(input().strip())
for a in range(n):
    l = 0
    m = int(input().strip())
    for i in range(m):
        if (i%3 and i%5) == 0:
            l+=i
    print(l)