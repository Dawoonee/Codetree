A = input()
cnt = 0
for a in range(len(A)):
    for b in range(a+1, len(A)):
        for c in range(b+1, len(A)):
            for d in range(c+1, len(A)):
                if A[a] =='(' and A[b] == '(' and A[c] == ')' and A[d] == ')' and a+1 == b and c+1 == d:
                    cnt += 1
print(cnt)