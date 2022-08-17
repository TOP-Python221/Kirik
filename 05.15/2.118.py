words = [word.strip('.,:!?-—"\'').lower()  for word in input().split()]

words_rev = list(reversed(words))

if words == words_rev:
    print('Предложение является словесным палиндромом')
else:
    print('Предложение  не является словесным палиндромом')


#Ввод:  "Herb the sage eats sage, the herb"
#Вывод: Предложение является словесным палиндромом