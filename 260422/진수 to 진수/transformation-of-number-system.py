a, b = map(int, input().split())
n = input()
N = int(n, a)

if N == 0:
    print('0')
else:
    arr = []
    while N > 0:
        r = N % b
        arr.append(str(r))
        N //= b
    print(''.join(arr[::-1]))
