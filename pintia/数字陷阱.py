n = int(input())
cnt, res = 0, 0
while n != res:
    res = n
    sum_bit = 0
    cnt += 1
    # 拆数
    while n != 0:
        sum_bit += n % 10
        n //= 10
    n = sum_bit * 3 + 1
    print(f'{cnt}:{n}')
