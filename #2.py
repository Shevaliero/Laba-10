'''2. Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа.
(Кудрявцев В.С)'''
def cor(x):
    if x<10:
        return x
    else:
        print(x)
        return cor(x%10 + x//10%10 + x//100)
x=int(input('x:'))
print(cor(x))

    
