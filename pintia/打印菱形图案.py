n = int(input())
# 输出上三角
for i in range(n//2+1):
    # 输出空格
    for j in range(n//2 - i):
        print('  ', end='')
    # 输出 *
    for j in range(2*i+1):
        print('* ', end='')
    # 换行
    print()
# 输出下三角
for i in range(n//2):
    for j in range(i+1):
        print('  ', end='')
    for j in range(2*(n//2 - i), 1, -1):
        print('* ', end='')
    # 换行
    print()