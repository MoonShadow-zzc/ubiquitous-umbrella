
pin = list(map(int, input().split()))
n = pin[0]
lst = pin[1:]
most_num = lst[0]
max_cnt = lst.count(lst[0])
for num in lst:
    if lst.count(num) > max_cnt:
        most_num = num
        max_cnt = lst.count(num)

print(most_num, max_cnt)

