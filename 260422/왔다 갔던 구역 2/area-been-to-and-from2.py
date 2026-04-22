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
        for j in range(start, start + x[i]+1):
            arr[j] += 1
        start = j

    else:
        # arr[start] -= 1
        for j in range(start , start- x[i]-1 , -1):
            arr[j] += 1
        start = j
answer = 0
cnt = 0
for z in arr:
    if z >= 2:
        cnt += 1
    else:
        if cnt == 0:
            continue
        answer += cnt-1
        cnt = 0
print(answer)