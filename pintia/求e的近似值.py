n = int(input())
e, part = 1.0, 1.0
for i in range(n):
    part /= i+1
    e += part
print(f'{e:.8f}')