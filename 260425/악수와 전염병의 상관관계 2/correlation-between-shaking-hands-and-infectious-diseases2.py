N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

handshakes = sorted(handshakes, key= lambda x: x[0])

infection = [[0,P] for _ in range(N+1)]
infection[P][0] = 1

for t, x ,y in handshakes:
    if infection[x][0] == 1 and infection[x][1] > 0:
        infection[y][0] = 1
        infection[x][1] -= 1
    elif infection[y][0] == 1 and infection[y][1] > 0:
        infection[x][0] = 1
        infection[y][1] -= 1
    elif infection[x][0] == 1 and infection[y][0] == 1:
        if infection[x][1] > 0:
            infection[x][1] -= 1
        if infection[y][1] > 0:
            infection[y][1] -= 1

print(''.join(map(str, [infection[i][0] for i in range(1, N+1)])))