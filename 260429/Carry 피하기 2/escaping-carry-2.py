n = int(input())
arr = [int(input()) for _ in range(n)]

max_val = -1
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a, b, c = str(arr[i]), str(arr[j]), str(arr[k])
            u, q, o = '0'*(5-len(a)) + a, '0'*(5-len(b)) + b, '0'*(5-len(c)) + c
            carry = False
            for z in range(5):
                t = int(u[z]) + int(q[z]) + int(o[z])
                if t >= 10:
                    carry = True
            if not carry:
                max_val = max(max_val, int(a) + int(b) + int(c))
print(max_val)
