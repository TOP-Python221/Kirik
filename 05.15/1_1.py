s = input('Введите e-mail: \n')

if '@' in s and '.' in s and s.index('@') != s.index('.')  :
    print('Верно')
            
else:  
    print('Неверно')