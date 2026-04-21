a, b, c = map(int, input().split())

z = a - 11
s = b - 11
d = c - 11

def check(a, b, c):
    x = a * 10000 + b * 100 + c
    if x >= 111111:
        return True
    else:
        return False

if check(a, b, c):
    if s < 0 :
        z -= 1
        s += 23
    if d < 0 :
        s -= 1
        d += 59
    answer = z*24*60 + s*60 + d
    print(answer)
else:
    print(-1)