def foo(a, arr=[]):
    arr.append(a)
    print(arr)


foo(1)
foo(2)


# значение переменных по умолчанию инициализируется ровно 1 раз - в момент
# компиляции байт-кода
def bar(a, *, b):  # звездочка указывает,
    # что надо именовать аргументы! Чтоб код был читабельнее
    ...


bar(1, b=2)

x = y = 1

x, y = y, x  # справа должен быть итерируемый объект (в данном случае tupple)

rectangle = (0, 0), (4, 4)
(x1, x2), (y1, y2) = rectangle
print((x1 := 5), y2)

first, *others, second = range(1, 10, 2)

print(others, type(others))

list_temp = [list(range(1, 10))] * 5
list_temp[0][0] = 999_999
print(list_temp)  # лежат 5 одинаковых списков

a, *temp = [1, 2, 3, 4, 5]
print(temp)
print('___________________________')
for a, *b in [range(5), range(3)]:
    print(b)

import dis  # че делает интерпретатор

dis.dis("first, *rest = ('a','b','c')")


def fhh1():
    print(globals())


fhh1()


def f():
    print(i)


for i in range(1, 5):
    f()

# поиск имени происходит динамически
# print(filter(lambda y: y > 19, list(map(lambda x: x *= 2, list(range(1, 15))))))
a = [x ** 2 for x in range(39)]  # внутри устроено как list(map(.....))
# list(range(5)) - list обходит все элементы нашего итератора, добавляя их в список


