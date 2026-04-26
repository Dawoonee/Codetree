commands = input()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0
x, y = 0, 0
time = 0
for com in commands:
    if com == 'R':
        d += 1
        if d > 3:
            d = 0
        time += 1
    elif com == 'L':
        d -= 1
        if d < 0:
            d = 3
        time += 1
    elif com == 'F':
        x += dx[d]
        y += dy[d]
        time += 1
    if x == 0 and y == 0:
        exit(print(time))
print(-1)
        