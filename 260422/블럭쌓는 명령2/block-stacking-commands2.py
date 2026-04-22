n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

arr = [0]*(n+1)
for a, b in commands:
    for j in range(a, b+1):
        arr[j] += 1
print(max(arr))