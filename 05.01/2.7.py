s = 0
n = int(input('Введите количество чисел:\n'))
print('Вводите числа\n')
for i in range(n):
    i = int(input())
    s = s + i
print(s)