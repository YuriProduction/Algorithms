a = '''1
2
3
4'''  # иначе ошибка
print(a)
b = "123"'456'
print(b)
# экранированная строка - начинающаяся со слэша
print('\xab13')
print('\xac')
# UTF-8,16,32 - способы кодирования UNICODE в байты для записи (в файл например)

print(list(map(ord, 'Hello, world!')))
print('\u0068')

chunk = "My String".encode("utf-8")
print(chunk.decode("utf-8"))
print(0x48)

from functools import wraps

DECOR_ENABLED = True


def decor(func):
    """Function - decorator"""

    @wraps(func)
    def inner(*args, **kwargs):
        """|Inner func documentation|"""
        print("Start")
        func(args, kwargs)
        print("Finish")
        # wraps(func) делает inner.__doc__ = func.__doc__ и тд.

    return inner if DECOR_ENABLED else func  # то есть мы можем выключить декоратор


@decor
def bar(x: int):
    """Testing function"""
    print(x)


print(bar.__name__, bar.__doc__, bar.__module__)


def min_element(arr: list) -> int:
    if len(arr) == 2:
        return arr[0] if arr[0] < arr[1] else arr[1]
    sub_min = min_element(arr[1:])
    return arr[0] if arr[0] < sub_min else sub_min


print(min_element([5, 2, -1, 123, 132, 1, 23, 0]))

arr1 = [1, 2, 3, 4, 5]
arr2 = arr1[1:]
arr2[2] = 5
print(arr2)
print(arr1)


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    print("Функция вызывана с параметром {}".format(n))
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


def decor_noth(func):
    arr = []
    print("arr снаружи", arr)

    def inner_foo(a):
        print("arr внутри", arr)
        if a in arr:
            print(a)
        else:
            print(f"{a} not in arr")
            arr.append(a)
        func(a)

    return inner_foo


@decor_noth  # в этом месте происходит do_nothing = decor_noth(do_nothing)
def do_nothing(val: int):
    pass

# do_nothing(1)
# do_nothing(1)
# do_nothing(1)
# do_nothing(2)
# do_nothing(2)
# do_nothing(3)
# do_nothing(1)
# do_nothing(2)
