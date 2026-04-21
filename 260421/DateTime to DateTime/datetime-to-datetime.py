a, b, c = map(int, input().split())

z = a - 11
s = b - 11
d = c - 11
if s < 0:
    z -= 1
    s += 23
if d < 0:
    s -= 1
    d += 59
print(z*24*60 + s*60 + d)