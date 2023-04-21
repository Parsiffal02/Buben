c=0
while True:
    a=int(input('Введите число. Когда устанете введите 0: '))
    if a==0:
        break
    if a%2==0:
        c+=1
print('Всего четных чисел: ', c)