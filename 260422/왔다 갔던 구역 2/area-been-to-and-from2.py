n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)
arr = [0]*2001
start = 1000
# arr[1000] = 1
for i in range(n):
    # print(arr[989:1003])
    if dir[i] == 'R':
        # arr[start] -= 1
        for j in range(start, start + x[i]):
            arr[j] += 1
        start += x[i]

    else:
        # arr[start] -= 1
        for j in range(start- x[i], start):
            arr[j] += 1
        start -= x[i]
answer = 0
for z in arr:
    if z >= 2:
        answer += 1
print(answer)