day = input("请输入年月日(格式举例: 2000-01-05)：")
year = int(day[:4])
month = int(day[5:7])
sun = int(day[8:10])
print(year, month, sun)
f_run = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
tall_day = 0
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    f_run[1] = 29
for i in range(month - 1):
    tall_day += f_run[i]
tall_day += sun
print(day + "是当年的第" + str(tall_day) + "天")
