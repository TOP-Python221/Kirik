words = [word.strip('.,:!?-—"\'')  for word in input().split()]
print(words)


#Ввод:  "Contractions include: don’t, isn’t, and wouldn’t."
#Вывод: ['Contractions', 'include', 'don’t', 'isn’t', 'and', 'wouldn’t']