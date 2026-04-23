n = int(input())
arr = [int(input()) for _ in range(n)]

max_cnt = 0
cnt = 0

for i in range(n):
    if cnt == 0 or arr[i-1] < arr[i]:
        cnt += 1
    else:
        cnt = 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)