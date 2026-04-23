N = int(input())
arr = [int(input()) for _ in range(N)]

max_cnt = 0
cnt = 0

for i in range(N):
    if cnt == 0 or abs(arr[i-1] + arr[i]) > abs(arr[i]):
        cnt += 1
    elif abs(arr[i-1] + arr[i]) < abs(arr[i]):
        cnt = 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
