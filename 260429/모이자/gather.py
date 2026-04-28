n = int(input())
A = list(map(int, input().split()))

answer = []

for i in range(n):
    a = 0
    for j in range(n):
       a += (abs(i-j)*A[j])
    answer.append(a)
print(min(answer))