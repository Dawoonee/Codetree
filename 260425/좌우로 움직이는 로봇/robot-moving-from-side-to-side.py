n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

a = [0]*2000001
pos_a = 0
time_a = 1
for i in range(n):
    if d[i] == 'R':
        for x in range(1, t[i]+1):
            a[time_a] = pos_a+x
            time_a += 1
        pos_a += t[i]
    elif d[i] == 'L':
        for x in range(1, t[i]+1):
            a[time_a] = pos_a-x
            time_a += 1
        pos_a -= t[i]

b= [0]*2000001
pos_b = 0
time_b = 1
for i in range(m):
    if d_b[i] == 'R':
        for x in range(1, t_b[i]+1):
            b[time_b] = pos_b+x
            time_b += 1
        pos_b += t_b[i]
    elif d_b[i] == 'L':
        for x in range(1, t_b[i]+1):
            b[time_b] = pos_b-x
            time_b += 1
        pos_b -= t_b[i]
cnt = 0
max_time = max(time_a, time_b)
for i in range(time_a, max_time):
    a[i] = pos_a
for i in range(time_b, max_time):
    b[i] = pos_b

for i in range(1, max_time):
    if a[i-1] != b[i-1] and a[i] == b[i]:
        cnt += 1

print(cnt)