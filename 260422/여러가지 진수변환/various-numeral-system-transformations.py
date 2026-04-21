N, B = map(int, input().split())
if B == 4:
    arr = []
    i  = 0
    while 4**i <= N:
        i += 1
    while N > 0:
        if i == 0:
            break
        a = N // 4**(i-1)
        arr. append(a)
        N -= 4**(i-1)*a
        i -= 1
    print(''.join(map(str, arr)))
elif B == 8:
    a = oct(N)
    print(a[2:])
