'''Задание 1
Пользователь вводит с клавиатуры размер стороны квадрата. Требуется отобразить на экран заполненный
квадрат. Размер стороны равен введённому размеру. Например, если пользователь ввёл 3 на экране будет
выведено:
***
***
*** '''
x=int(input('Введите размер стороны квадрата: '))
print(('*'*x),"\n"+'*'*x,'',"\n"+'*'*x,end='')

#Или так.
x=int(input('\nВведите размер стороны квадрата: '))
z=('*'*x)
for i in range(x):
    print(z)


'''Задание 2
Пользователь вводит с клавиатуры ширину и высоту прямоугольника. Требуется отобразить на экран
заполненный прямоугольник с указанными высотой и шириной. Например, если пользователь ввёл высоту 3,
а ширину 5 на экране будет выведено:
*****
*****
*****'''

x=int(input('Введите ширину квадрата: '))
y=int(input('Введите высоту квадрата: '))
z=('*'*x)
for i in range(y):
    print(z)

''' Задание 3
Пользователь вводит с клавиатуры размер стороны квадрата. Требуется отобразить на экран незаполненный
квадрат (отображаются только границы квадрата). Размер стороны равен введённому размеру.'''

x=int(input('Введите размер стороны квадрата: '))
for i in range(x-1):
    if i==0 :
        print('*'*(x))
    if i>0 :
        print('*'+(' '*(x-2)+'*'))
    if i==x-2:
        print('*'*x)


'''Задание 4
Пользователь вводит с клавиатуры длину и ширину прямоугольника. Требуется отобразить на экран 
незаполненный прямоугольник (отображаются только границы прямоугольника). Размер длины и ширины равен
введенным данным.'''

x=int(input('Введите ширину прямоугольника: '))
y=int(input('Введите длину прямоугольника: '))
for i in range(y-1):
    if i==0 :
        print('*'*(x))
    if i>0 :
        print('*'+(' '*(x-2)+'*'))
    if i==y-2:
        print('*'*x)