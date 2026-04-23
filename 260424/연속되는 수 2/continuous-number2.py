n = int(input())
arr = [int(input()) for _ in range(n)]
max_cnt = 0
cnt = 1
for i in range(1, n):
    if arr[i-1] == arr[i]:
        cnt += 1
    elif arr[i-1] != arr[i]:
        cnt = 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)