'''Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n.
(Кудрявцев Владислав)'''
def factr(x):   #рекурсивно
    global countr
    if x!=1:
        countr+=1
        return factr(x-1)*x
    else:
        countr+=1
        return 1
def facti(x):   #Итеративно
    global counti
    res=1
    for i in range(x):
        counti+=1
        res*=i+1
    return res
countr=0
counti=0
x=int(input('x:'))
print(f'Rekursion:{factr(x)}\n worked {countr} times')
print(f'Iteration:{facti(x)}\n worked {counti} times')
#Тут задачи одинаковы по сложности, по этому лучшим вариантом будет итеративный
#способ так как он менее затратный по памяти
