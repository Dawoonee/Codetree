n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

a = [0]*1001
b = [0]*1001
i, j = 0, 0
time = 1
for z in range(n):
    if d[z] == 'R':
        for c in range(i, i + t[z]):
            a[time] = c + 1
            time += 1
        i = i + t[z]
    else:
        for c in range(i , i-t[z], -1):
            a[time] = c -1
            time += 1
        i = i - t[z]

time_b = 1
for x in range(m):
    if d2[x] == 'R':
        for c in range(j, j + t2[x]):
            b[time_b] = c + 1
            time_b += 1
        j = j + t2[x]
    else:
        for c in range(j, j-t2[x], -1):
            b[time_b] = c - 1
            time_b += 1
        j = j - t2[x]

for y in range(1, 11001):
    if a[y] == b[y]:
        answer = y 
        break
print(answer)