s = input()
n = len(s) - s.count(" ")
print(f'{n*80//100} руб. {n*80%100} коп.')