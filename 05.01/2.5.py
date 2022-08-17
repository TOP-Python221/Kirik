s = []
i = int(input('Введите числа, кратные или не кратные 7: \n'))
while i % 7 == 0 :
    s.append(i)
    i = int(input())
for i in s:        
     print(i, end = ' ')
    
 