'''Задание 1
Напишите программу, которая запрашивает два целых числа x и y, после чего вычисляет и выводит
значение x в степени y.'''

#1 Вариант
x=int(input('Введите первое целое число x: '))
y=int(input('Введите второе целое число y: '))
print('Значение x в степени y =', x**y)


#2 Вариант
x=int(input('Введите первое целое число x: '))
y=int(input('Введите второе целое число y: '))
z=1
for i in range(y):
    z=z*x
print('Значение x в степени y =',z)

'''Задание 2
Подсчитать количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры.'''

x=0
for i in range(100,1000):
    a=str(i)
    a1=i//100
    a2=i%100//10
    a3=i%10
    if a1==a2 or a1==a3 or a2==a3:
        x=x+1
print('Количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры = ',x)

'''Задание 3
Подсчитать количество целых чисел в диапазоне от 100 до 9999 у которых все цифры разные.'''

x=0
y=0
for i in range(100,1000):
    a=str(i)
    a1=i//100
    a2=i%100//10
    a3=i%10
    if i<1000:
        if a1!=a2 and a1!=a3 and a2!=a3:
            x=x+1
for i in range(1000,9999):
    a=str(i)
    a1=i//1000
    a2=i%1000//100
    a3=i%100//10
    a4=i%10
    if i>=1000:
        if a1!=a2 and a1!=a3 and a1!=a4 and a2!=a3 and a2!=a4 and a3!=a4:
            y=y+1
print('Количество целых чисел в диапазоне от 100 до 9999 у которых все цифры разные = ',x+y)


'''Задание 4
Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и
вывести обратно на экран.'''

n=int(input('Введите целое число: '))
a=0
i=0
while n>0:
    num=n%10
    if num!=3 and num!=6:
        a=a+num*10**i
        i=i+1
    n=n//10
print('Введенное число без цифр 3 и 6 = ',a)

