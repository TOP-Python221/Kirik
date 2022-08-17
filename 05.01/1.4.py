y1 = input('Введите букву от a до h: ')
x1 = int(input('Введите цифру от 1 до 8: '))
y2 = input('Введите букву от a до h: ')
x2 = int(input('Введите цифру от 1 до 8: '))
i1 = x1 + 1
i2 = x1 - 1
j1 = ord(y1) + 1
j2 = ord(y1) - 1
if (x1 == x2 or x2 == i1 or x2 == i2) or (y1 == y2 or y1 == chr(j1) or y1 == chr(j2)):
    print('Да')
else: 
    print ('Нет')