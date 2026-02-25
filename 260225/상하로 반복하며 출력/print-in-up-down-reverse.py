N = int(input())

arr = [[i for i in range(1,N+1)] for _ in range(N)]

for i in range(N):
    if i % 2 != 0:
        for j in range(N):
            arr[N - 1 - j][i] = j + 1
            
    else:
        for j in range(N):
            arr[j][i] = j + 1

for row in arr:
    for val in row:
        print(val, end="")
    print()
