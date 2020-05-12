'''3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
(Кудрявцев В.С)'''
import numpy as np
import random
#Рекурсия
def maxr(a,n,m,mx,mxn,mxm):         #n - столбец, m - строка 
    l=len(a)
    if m==len(a[n]):                #переход на следующюю строку
        n+=1
        m=0
    if n==l:                #на этом рекурсия вернет значения
        return mx, mxn ,mxm
    if a[n][m]>mx:      #условие при котором запишется новый элемент, который больше
        mx=a[n][m]
        mxn=n
        mxm=m
    m+=1                 
    return maxr(a,n,m,mx,mxn,mxm)
#Итерация
def maxi(a,n,m,mx,mxn,mxm):
    l=len(a)
    for i in range(l):
        for j in range(l):
            if a[i][j]>mx:
                mx=a[i][j]
                mxn=i
                mxm=j
    return mx,mxn,mxm
n=int(input('n:'))
m=n
a=np.zeros((n,m),dtype=int)
for i in range(len(a)):
    for j in range(len(a)):
        a[i][j]=random.randint(0,10)
print(a)
print(f'Rekursion:{maxr(a,0,0,0,0,0)}')
print(f'Iteration:{maxi(a,0,0,0,0,0)}')
#Тут так же итеративный вариант будет лучшим выбором ибо занимает куда меньше
#строк и к тому же куда проще для понимания(на рекурсивный способ ушло несколько
#часов, а на итеративный минуты 2)
    
    
    
