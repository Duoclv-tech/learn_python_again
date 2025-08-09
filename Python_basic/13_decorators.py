"""
PHẦN 13: DECORATORS TRONG PYTHON
================================

Bài tập về function decorators, class decorators, built-in decorators, decorator có tham số,
và functools.wraps.
"""

# CÂU HỎI 1: Function decorators cơ bản
# a) Viết decorator timeit đo thời gian chạy của hàm
# b) Áp dụng timeit cho một hàm tính tổng 1..n

# Code của bạn ở đây:



# CÂU HỎI 2: functools.wraps
# a) Viết decorator logger in tên hàm và đối số, đảm bảo giữ nguyên __name__ và __doc__ bằng wraps

# Code của bạn ở đây:



# CÂU HỎI 3: Decorator với parameters
# a) Viết decorator repeat(times=1) để chạy hàm nhiều lần

# Code của bạn ở đây:



# CÂU HỎI 4: Class decorators
# a) Viết class decorator add_method thêm một phương thức say_hello(self) vào class mục tiêu

# Code của bạn ở đây:



# CÂU HỎI 5: Built-in decorators
# a) Viết class Temperature với @property celsius và fahrenheit (giống phần OOP, tóm tắt)
# b) Viết class Util với @staticmethod is_even(n) và @classmethod from_string(cls, raw)

# Code của bạn ở đây:



'''
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

import time
from functools import wraps

# CÂU HỎI 1:
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = (time.perf_counter() - start) * 1000
            print(f"{func.__name__} chạy trong {elapsed:.2f} ms")
    return wrapper

@timeit
def sum_n(n: int) -> int:
    return sum(range(1, n + 1))

print("Tổng 1..1_000_00:", sum_n(100_000))

# CÂU HỎI 2:
def logger(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"Gọi {func.__name__} với args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} -> {result}")
        return result
    return inner

@logger
def multiply(a, b):
    """Nhân hai số"""
    return a * b

multiply(6, 7)
print(multiply.__name__, '-', multiply.__doc__)

# CÂU HỎI 3:
def repeat(times=1):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            last = None
            for _ in range(times):
                last = func(*args, **kwargs)
            return last
        return inner
    return decorator

@repeat(times=3)
def hello(name="Python"):
    print(f"Xin chào {name}")

hello("Decorators")

# CÂU HỎI 4:
def add_method(cls):
    def say_hello(self):
        print(f"Hello from {self.__class__.__name__}")
    setattr(cls, "say_hello", say_hello)
    return cls

@add_method
class MyClass:
    pass

MyClass().say_hello()

# CÂU HỎI 5:
class Temperature:
    def __init__(self, celsius: float):
        self._c = float(celsius)

    @property
    def celsius(self):
        return self._c

    @celsius.setter
    def celsius(self, value):
        self._c = float(value)

    @property
    def fahrenheit(self):
        return self._c * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._c = (float(value) - 32) * 5 / 9

class Util:
    @staticmethod
    def is_even(n: int) -> bool:
        return n % 2 == 0

    @classmethod
    def from_string(cls, raw: str):
        return cls()

print("2 chẵn?", Util.is_even(2))


# BÀI TẬP NÂNG CAO 1:
# Viết decorator retry(max_tries=3, delay=0.1, exceptions=(Exception,)) để tự động thử lại
# khi hàm ném ra exceptions chỉ định. Gợi ý: time.sleep, wraps.

# BÀI TẬP NÂNG CAO 2:
# Viết decorator memoize_ttl(ttl_seconds=60) để cache kết quả theo tham số trong thời gian TTL.
# Gợi ý: dùng dict với (args, frozenset(kwargs.items())) làm key, lưu (value, expire_ts).
'''