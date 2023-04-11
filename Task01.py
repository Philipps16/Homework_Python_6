# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_number = int(input())
defination = int(input())
finish_number = int(input())

list_ = []
while finish_number > 0:
    new_number = first_number + (finish_number - 1)*defination
    list_.append(new_number)
    finish_number-=1
print (sorted(list_))
