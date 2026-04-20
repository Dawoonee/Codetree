a, b, c, d = map(int, input().split())
z = c-a
x = d-b

if x < 0:
    z -= 1
    x += 60
print(60*z+x)