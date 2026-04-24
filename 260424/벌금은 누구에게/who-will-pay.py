N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
arr = [0]*(N+1)
for i in student:
    arr[i] += 1
answer = 0
for i in range(N):
    if arr[i] >= K:
        answer = i
        break
if answer == 0:
    print(-1)
else:
    print(answer)