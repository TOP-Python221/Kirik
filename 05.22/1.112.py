s_inp = [int(i) for i  in input('Введите не менее четырех чисел, разделяя их пробелом: \n').split()]

if len(s_inp) < 4:
    print('Ошибка ввода, должно быть введено не менее четырех чисел')
else:   
    print(f'Оригинальный список {s_inp}')
    s_inp.sort()
    print(f'Измененный список   {s_inp[1:-1]}')  
   
#Ввод: 1 2 3
#Вывод: Ошибка ввода, должно быть введено не менее четырех чисел
#Ввод: 99 22 -5 0 15 45 65
#Вывод Оригинальный список [99, 22, -5, 0, 15, 45, 65]
#      Измененный список   [0, 15, 22, 45, 65]