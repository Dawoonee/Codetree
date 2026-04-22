a, b = map(int, input().split())
n = input()
N = int(n, a)
arr = []
i  = 0
while b**i <= N:
    i += 1
while N > 0:
    if i == 0:
        break
    a = N // b**(i-1)
    arr. append(a)
    N -= b**(i-1)*a
    i -= 1
print(''.join(map(str, arr)))