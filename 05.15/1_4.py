l = input('Введите числа:\n')
l1 = list(map(int, l))
if sum(l1[:3]) == sum(l1[-3:]):
    print('Да')
else:
    print('Нет')