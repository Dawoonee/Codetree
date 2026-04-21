def check (m1, d1, m2, d2):
    a, b = m1*100 + d1, m2*100 + d2
    if a <= b:
        return True
    else:
        return False
m1, d1, m2, d2 = map(int, input().split())
arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
#True 오른쪽 False 왼쪽
if check(m1, d1, m2, d2):
    step = 0
    for i in range(m1+1, m2):
        step += arr[i]
    step += d2
    step = step - d1
    step = (1 + step)%7
    print(t[step])

else:
    step = 0
    for i in range(m2+1, m1):
        step += arr[i]
    step += d1
    step = step - d2
    step = (1 - step)%7
    print(t[step])
