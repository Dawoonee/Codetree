
m1, d1, m2, d2 = map(int, input().split())
arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
#True 오른쪽 False 왼쪽
def sum_d(m, d):
    return sum(arr[:m]) + d
a = sum_d(m1, d1)
b = sum_d(m2, d2)
dif = b - a
step = (1 + dif)%7
print(t[step])
