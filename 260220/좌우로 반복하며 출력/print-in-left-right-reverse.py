N = int(input())

for prt in range(N):
    if prt%2 == 0:
        for i in range(1,N+1):
            print(i,end='')
    
    else:
        for i in range(N, 0, -1):
            print(i,end='')
    print()