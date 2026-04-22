n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

arr = [['',0] for _ in range(200001)]
start = 100000
# arr[1000] = 1
for i in range(n):

    if dir[i] == 'R':
        # arr[start] -= 1
        for j in range(start, start + x[i]):
            arr[j][1] += 1
            arr[j][0] = 'B'
        start  += x[i] -1

    else:
        # arr[start] -= 1
        for j in range(start- x[i], start):
            arr[j+1][1] += 1
            arr[j+1][0] = 'W'
        start -= x[i] -1

a, b, c = 0, 0, 0
#흰 , 검 , 회
for i in range(200001):
    if arr[i][1] > 3:
        arr[i][0] = 'G'
for z, x in arr:
    if z == 'W':
        a += 1
    elif z == 'B':
        b += 1
    elif z == 'G':
        c += 1

print(f'{a} {b} {c}')