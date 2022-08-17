words = [ word for word in input().split()]

for i in range(len(words) - 1):
    if i < (len(words) - 2):
        words[i] = words[i] + ','
    else:
        words[i] =  words[i] + ' и'
    
else:
    words[i] = words[i]
print(*words)

#Ввод:яблоки апельсины бананы лимоны
#Вывод:яблоки, апельсины, бананы и лимоны