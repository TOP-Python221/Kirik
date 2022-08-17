sm = 0
n = int(input('Введите число n: '))
print(f'Введите {n} чисел: ')
for i in range(1, n + 1):
    i = int(input())
    if i > 0: 
        sm += i  
print(sm)
