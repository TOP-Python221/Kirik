i = 1
j = 1
n = int(input('Введите количество чисел:\n'))
if n > 1:
    print(i, j, end = ' ')
    for f in range(2, n ):
        i, j = j, i + j
        print(j, end = ' ')
else:
    print(i, end = ' ')