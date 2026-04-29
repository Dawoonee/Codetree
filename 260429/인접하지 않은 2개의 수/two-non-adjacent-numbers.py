n = int(input())
numbers = list(map(int, input().split()))
max_val = 0
for i in range(n):
    for j in range(n):
        c = numbers[i]
        if abs(i-j) == 0 or abs(i-j) == 1:
            continue
        c += numbers[j]
        max_val = max(max_val, c)
print(max_val)