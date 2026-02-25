n = int(input())
arr = [[0]*n for _ in range(n)]
cnt = 1

for i in range(n):
    for j in range(n):
        arr[i][j] = cnt
        cnt += 1
        if cnt > 9:
            cnt = 1
    print(*arr[i])