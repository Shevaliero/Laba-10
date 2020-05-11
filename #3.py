'''3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
(Кудрявцев В.С)'''
import numpy as np
import random
def maxi(a,n,m,mx,mxn,mxm):         #n - столбец, m - строка 
    l=len(a)
    if n==l-1:                #переход на следующюю строку
        m+=1
        n=0
    if a[n][m]>mx:      #условие при котором запишется новый элемент, который больше
        mx=a[n][m]
        mxn=n
        mxm=m
    if m==l-1:                #на этом рекурсия вернет значения
        return mx, mxn ,mxm
    n+=1                 
    return maxi(a,n,m,mx,mxn,mxm)
n=int(input('n:'))
m=n
a=np.zeros((n,m),dtype=int)
for i in range(len(a)):
    for j in range(len(a)):
        a[i][j]=random.randint(0,10)
print(a)
print(maxi(a,0,0,0,0,0))
    
    
    
