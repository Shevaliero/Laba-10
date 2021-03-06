'''2. Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа.
(Кудрявцев В.С)'''
def rcor(x):    #Рекурсивно
    if x<10:
        return x
    else:
        return rcor(x%10 + x//10%10 + x//100)
def icor(x):    #Итеративно
    while x>=10:
        x=x%10 + x//10%10 + x//100
    return x
x=int(input('x:'))
print(f'Rekursion:{rcor(x)}')
print(f'Iteration:{icor(x)}')
#Тут ситуация та же, что и с факториалом, задачи практически равны по сложности
#по этому итеративный способ будет лучше, к тому же итеративный вариант
#занимает меньше строк

    
