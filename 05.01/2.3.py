sm = 0
n = int(input('Введите число n: '))
d = 1
for d in range(1, n + 1):
    if n % d == 0: 
        sm += d  
        d = d + 1
print(sm)
