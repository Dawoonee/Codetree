m1, d1, m2, d2 = map(int, input().split())
A = input()

arr = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def sum_d(m, d):
    return sum(arr[:m]) + d
a = sum_d(m1, d1)
b = sum_d(m2, d2)
diff = b - a
# print(diff)
answer = (diff + 1)//7
if (diff + 1)%7 == t.index(A):
    answer += 1
print(answer)