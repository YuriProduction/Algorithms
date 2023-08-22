def sum(a, b) -> int:
    return a + b


def mul(a, b) -> int:
    return a * b


sum.__code__ = mul.__code__

print(sum(3, 2))
...
print(type(print(None)))
print(type(None))


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b


a = A(1, 2)
b = A(1, 3)
a_2 = a

print(a_2 is a)
print(type(False))

True and print(sum(3, 3))
print(False and True)
assert a is a_2, "a is s_2"
print(2 ** 12031)
a = [[0] * 3] * 3
a[0][0] = 1
print(a)

a = list(range(20))
print(a[:-10:-2])
print(a[-6:-10:-2])
b = a[:]
b.append(345)
print(a)
print(type(set()))
