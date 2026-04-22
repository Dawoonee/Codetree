n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]


arr = [0]*201
for a, b in segments:
    for j in range(a+100, b+101):
        arr[j] += 1
print(max(arr))