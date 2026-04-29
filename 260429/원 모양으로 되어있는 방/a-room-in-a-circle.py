n = int(input())
a = [int(input()) for _ in range(n)]
min_val = 1000000000000000000000001
for i in range(n):
    c = 0
    for j in range(n):
        if i <= j:
            r = abs(i-j)
            c += (a[j]*r)

        else:
            r = (n-i) + j
            c += (a[j]*r)
    min_val = min(min_val, c)
print(min_val)
