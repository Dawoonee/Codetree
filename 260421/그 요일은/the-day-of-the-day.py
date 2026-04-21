m1, d1, m2, d2 = map(int, input().split())
A = input()
# print(m1, d1, m2, d2)
arr = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def sum_d(m, d):
    return sum(arr[:m],d)
one = sum_d(m1, d1)
two = sum_d(m2, d2)
# print(one, two)
diff = two - one
# print(diff)
answer = diff//7
if diff%7 >= t.index(A):
    answer += 1
print(answer)