cortezh = (100,)
[first] = cortezh
print(first)
print([1, 2, 3, 4, 5][::2])
print(tuple(reversed((1, 2, 3))))  # reverse не выделяет память
print((1, 2, 3)[-1::-1])  # а здесь создается новый кортеж
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr[::2] = [55, 66, 77, 88, 99]
print("arr: ", arr, sep='\t')
from collections import namedtuple

# фабрика классов, для использования легковесных классов
Person = namedtuple("Person", ["name", "age"])
p1 = Person("Gregory", "57")
print(p1.age)

# reversed - некий ленивый объект перечисляющий элементы в обратном порядке
print((1, 2, 4) > (1, 2, 3, 4))  # сначала по первой координате, затем по второй и тд

temp_list = [(1, 2), (1, 3), (2, 2)]
temp_list.sort(key=lambda x: (x[1], x[0]), reverse=True)
print(temp_list)
arr.reverse()
print(arr)
del arr[0]
print(arr)
from collections import defaultdict

g = {'b': {'c'}, 'a': {'b'}}
g['b'].add('a')
print(g)
# g['c'].add('a') #KeyError
g = defaultdict(set, {'b': {'c'}, 'a': {'b'}})
g['c'].add('a')
# как раз если значение отсутствует все будет норм
print(g)
from collections import Counter

c = Counter(["1", "1", "1", "2"])
c["1"] += 1
print(c)
