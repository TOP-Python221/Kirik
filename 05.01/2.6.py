m = int(input('Введите число m: \n'))
n = int(input('Введите число n: \n'))
if m > n:
    print('Не соблюднено условие задачи \nm <= n')        
else:
    for i in range( m, n + 1):
        print(i, end = ' ')
    