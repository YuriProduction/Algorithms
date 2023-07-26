class Counter:
    arr_instances = []  # типо статическое поле, атрибут не экземпляра, а класса

    def __init__(self, initial_count=0):  # не совсем конструктор, просто метод
        self.count = initial_count  # нет декларации для полей в питоне, поэтому надо писать self
        Counter.arr_instances.append(self)

    def get(self):
        return self.count

    def increment(self):
        self.count += 1


a = Counter(1)
b = Counter(2)
c = Counter(3)
assert a.arr_instances is b.arr_instances
print(Counter.arr_instances)
# в питоне область видимости(scope) - это словарь, то есть когда мы ищем имя мы
# ищем его в словаре
print(a.__class__,
      a.__dict__,
      a.__dict__['count'] == a.count
      )

print(a)

print(a.arr_instances is Counter.arr_instances)

del a

# ссылка остается
print(b.arr_instances)
print(b.arr_instances[0].count)


class tempClass(object):
    common_field = []


a1 = tempClass()
b1 = tempClass()
b1.common_field.append(1)
a1.common_field.append(2)  # он в своем словаре получается инкрементит
print(a1)


class Weird:  # cringe
    a = 1
    for _ in range(10):
        a += 1


print(Weird.a)
print(type(c.__class__))
b.some_type = 1  # legal because of dictionary sense

print(Weird.__dict__)
