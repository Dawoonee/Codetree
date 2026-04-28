a = int(input(), 2)
max_val = 0
for i in range(len(bin(a))-2):
    mask = 1 << i
    f = a^mask
    max_val = max(max_val, f)
print(max_val)