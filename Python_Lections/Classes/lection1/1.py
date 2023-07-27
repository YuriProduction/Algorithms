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
# but we can constraint this by __slots__

print(Weird.__dict__)


class Point(object):
    # __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def getX(self):
        return self.x


point = Point(1, 2)
point.x = 2
print(point)
print(Point.__dict__)

# point.z = 4 AttributeError


# @total_ordering
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print("Getting the radius...")
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        print("Setting the radius...")
        self._radius = value

    @property
    def area(self):
        return 3.14 * self._radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __eq__(self, other):
        return self._radius == other._radius


class BetterCircle(Circle):
    pass


better_circle = BetterCircle(5)
print('__________________________________________--')
print(better_circle)
print('__________________________________________--')
# Create a circle object
my_circle = Circle(5)

# Accessing the radius property (using the getter)
print(my_circle.radius)  # Output: Getting the radius... 5

# Using the area property (also a @property, but without a setter)
print(my_circle.area)  # Output: 78.5

# Setting the radius property (using the setter)
my_circle.radius = 7  # Output: Setting the radius...


# Trying to set a negative radius (raises a ValueError)
# my_circle.radius = -3  # Output: ValueError: Radius cannot be negative.


class A:
    def __init__(self, initial=0):
        self.value = initial


class B(A):
    def get(self):
        return self.value


b3 = B()
print(b3.__dict__)


class Base:
    def f(self):
        print("Base")


class A(Base):
    def f(self):
        print("A")
        super().f()  # super берет следующий класс из mro()
        # super = super(C,self) в данном случае


class B(Base):
    def f(self):
        print("B")
        super().f()


class C(A, B):
    pass


C().f()

assert C.mro() == [C, A, B, Base, object]


if True:
    ggg = 7

print(globals())