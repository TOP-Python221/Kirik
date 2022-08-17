words = [word.lower()  for word in input().split()]
vowels = 'aeiou'
wordpig = ''
for w in words:
    if w[0] in vowels:
        w += 'way '
        wordpig += w
    else:   
        for w2 in w:
                         
            if w2 in vowels:
                n = w.index(w2)
                w = w[n:] + w[:n] + 'ay '
                wordpig += w
                break
print(wordpig.rstrip())    

#Ввод: computer abba yellow apple
#Вывод: omputercay abbaway ellowyay appleway