n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
answer = 1000001
for i in range(1, n-1):
    a, b = x[0], y[0]
    c = 0
    for j in range(1, n-1):
        if i == j:
            continue
        c += (abs(a-x[j]) + abs(b-y[j]))
        a, b = x[j], y[j]
    c += (abs(a - x[-1]) + abs(b - y[-1]))
    answer = min(answer, c)
print(answer)