A = input()
cnt = 0
for i in range(len(A)):
    for j in range(len(A)):
        if i > j:
            continue
        if A[i]+A[j] == '()':
            cnt += 1
print(cnt)