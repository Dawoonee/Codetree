dirs = input()

x, y = 0, 0
Direction = 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in dirs:
    if i =='L':
        if Direction == 3:
            Direction = 0
        else:
            Direction += 1
    elif i == 'R':
        if Direction == 0:
            Direction = 3
        else:
            Direction -= 1
    elif i == 'F':
        x += dx[Direction]
        y += dy[Direction]
print(f'{x} {y}')
