y1 = input('Введите букву от a до h для клетки где находится ладья: ' )
x1 = int(input('Введите цифру от 1 до 8 для клетки где находится ладья: '))
y2 = input('Введите букву от a до h для клетки куда ладья должна пойти: ' )
x2 = int(input('Введите цифру от 1 до 8 для клетки куда ладья должна пойти: ' ))

if x1 == x2 or y1 == y2:
    print('Да')
else:
    print('Нет')

