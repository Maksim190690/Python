'''Задание 1
Пользователь вводит с клавиатуры время в секундах, прошедшее с начала дня. В зависимости от выбора
пользователя посчитать, сколько часов, минут и секунд осталось до полуночи.'''

x=int(input('Введите время в секундах, прошедшее с начала дня: '))
y=input("Выбирете в каких единицах посчитать, сколько осталось до полуночи: ,"
        "\nВ Часах 'ч'=,"
        "\nВ Минутах 'м'=,"
        "\nВ Секундах 'с'=,\n")
if y=='ч':
    print('До полуночи осталось: ',12-(x/60**2),'часов')
if y=='м':
    print('До полуночи осталось: ',(12*60)-(x/60),'минут')
if y=='с':
    print('До полуночи осталось: ',(12*60**2)-x,'секунд')


'''Задание 2
Пользователь вводит с клавиатуры диаметр окружности. В зависимости от выбора пользователя посчитать
площадь или периметр окружности.'''

x=int(input('Введите диаметр окружности: '))
y=input("Выбирете что посчитать: "
        "\nПлощадь окружности - нажмите 'п'"
        "\nПериметр окружности - нажмите 'р',\n")
if y=='п':
    print('Площадь окружности = ',(x**2/4)*3.14)
if y=='р':
    print('Периметр окружности = ',(x*3.14))

'''Задание 3
Пользователь вводит с клавиатуры стоимость одной игровой приставки, их количество и процент скидки.
В зависимости от выбора пользователя посчитать общую сумму заказа или стоимость одной приставки с учетом
скидки.'''

x1=int(input('Введите стоимость одной игровой приставки: '))
x2=int(input('Введите количество приставок: '))
x3=int(input('Введите процент скидки: '))
y=input("Выбирете, что посчитать: "
        "\nОбщую сумму заказа - нажмите '+'"
        "\nСтоимость одной приставки с учетом скидки - нажмите '-',\n")
if y=='+':
    print('Общая сумма заказа = ',x1*x2)
if y=='-':
    print('Cтоимость одной приставки с учетом скидки = ',x1-(x1*(x3/100)))


'''Задание 4
Пользователь вводит с клавиатуры размер файла в гигабайтах и скорость интернет-соединения в битах в
секунду. В зависимости от выбора пользователя посчитать,за сколько часов или минут, или секунд скачается файл.'''

x1=int(input('Введите размер файла в гигабайтах: '))
x2=int(input('Введите скорость интернет-соединения в битах в секунду: '))
y=input("Выбирете, что посчитать: "
        "\nЗа сколько часов скачается файл - нажмите 'ч'"
        "\nЗа сколько минут скачается файл - нажмите 'м'"
        "\nЗа сколько секунд скачается файл - нажмите 'с',\n")
if y=='ч':
    print('Файл скачается за ',((x1*(8*2^30))/x2)*60**2,'часа(ов).')# Значение битов в ГБ(8*2^30) взято с интернета
if y=='м':
    print('Файл скачается за ',((x1*(8*2^30))/x2)*60,'минут.')
if y=='с':
    print('Файл скачается за ',((x1*(8*2^30))/x2),'секунд')


'''Задание 5
Пользователь с клавиатуры вводит количество часов.Если полученное значение находится в диапазоне от 0 до
6 нужно вывести надпись Good Night, если в диапазоне от 6 до 13 Good Morning, если в диапазоне от 13 до 17 Good
Day, если в диапазоне от 17 до 0 Good Evening. Верхняя граница диапазона не включается. Например, число 6
относится к 6 до 13'''

x=int(input('Введите количество часов: '))
if 6 >x >0:
    print('Good Night')
if 6<=x<13:
    print('Good Morning')
if 13<=x<17:
	print('Good Day')
if 17<=x<=23:
    print('Good Evening')
if x==0:
	print('Good Evening')
