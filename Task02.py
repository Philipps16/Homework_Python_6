# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def numbers(list_, min_number, max_number):
    return [(i, el) for i, el in enumerate(list_) if min_number <= el <= max_number]

list_ = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print (list_)
print (numbers(list_, 2, 10))