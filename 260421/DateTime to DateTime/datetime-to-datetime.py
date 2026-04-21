a, b, c = map(int, input().split())

z = a - 11
s = b - 11
d = c - 11
if z <= 0:
    if s <= 0:
        if d <= 0:
            if z == 0 and s == 0 and d == 0:
                print(0)
            else:
                print(-1)
else:
    if s < 0:
        z -= 1
        s += 23
    if d < 0:
        s -= 1
        d += 59
    print(z*24*60 + s*60 + d)