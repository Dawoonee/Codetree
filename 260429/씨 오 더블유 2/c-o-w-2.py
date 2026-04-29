n = int(input())
S = input()
cnt = 0
for a in range(n):
    for b in range(a+1,n):
        for c in range(b+1, n):
            if S[a] == 'C' and S[b] =='O' and S[c] == 'W':
                cnt +=1
print(cnt)