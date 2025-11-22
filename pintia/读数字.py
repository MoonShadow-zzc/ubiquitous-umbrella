n = input()
length = len(n)
for i in n:
    if i == '-':
        print('fu', end='')
    elif i == '0':
        print('ling', end='')
    elif i == '1':
        print('yi', end='')
    elif i == '2':
        print('er', end='')
    elif i == '3':
        print('san', end='')
    elif i == '4':
        print('si', end='')
    elif i == '5':
        print('wu', end='')
    elif i == '6':
        print('liu', end='')
    elif i == '7':
        print('qi', end='')
    elif i == '8':
        print('ba', end='')
    else:
        print('jiu', end='')
    if length > 0:
        print(' ', end='')
    length -= 1
