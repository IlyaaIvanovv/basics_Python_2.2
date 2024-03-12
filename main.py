a = 25 + 25
b = a * 2
c = a / b
print('Ответ:', c)
# Ответ: 0.5


print(10 < 20)
print(10 > 5)
print(10 <= 10)
print(5 == 5)
print(5 != 5)

my_answer = 'True, True, True, True, False'
print(my_answer)


x = 120
if 0 <= x < 100:
    print('Верно')
else:
    print('Неверно')


height = 177
if height < 170:
    print('Низкий')
elif height > 180:
    print('Высокий')
else:
    print('Средний')

#Наличие в строке
text = 'Доброе утро и хорошего дня!'
if 'утро' in text:
    print('Слово встретилось')
else:
    print('Слово не встретилось')


#Должны выполняться оба (=и)
print((10 > 5) and (5 > 10))
print((10 > 5) and (5 > 2))
#Может выполнятся одно из (=или)
print((10 < 5) or (10 > 5))
# Ответ: False, True, True


color = 'green'
match color:
    case 'red' | 'yellow':
        print('Stop')
    case 'green':
        print('Go')
    case _:
        print('Not found')


#Високосными являются года, которые делятся на 4,
#за исключением столетий, которые делятся на 400.

year = int(input('Введите год'))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print('Обычный год')
else:
    print('Високосный год')