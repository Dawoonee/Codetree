N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

handshakes = sorted(handshakes, key= lambda x: x[0])

infection = [0]*(N+1)
infection[P] = 1

for t, x ,y in handshakes:
    if (x == P or y == P) and K >0:
        infection[x], infection[y] = 1, 1
        K -= 1
print(''.join(map(str, infection[1:])))