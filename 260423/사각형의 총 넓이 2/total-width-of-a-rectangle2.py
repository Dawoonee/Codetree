n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

#x = x2 - x1
#h = y2 - y1
#첫 번째 그 이후에
answer = (x2[0] - x1[0]) * (y2[0] - y1[0])
for i in range(1, n):
    x = x2[i-1] - x1[i]
    h = y2[i] - y1[i]
    answer += (x*h)
print(answer)