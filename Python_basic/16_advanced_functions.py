"""
PHẦN 16: ADVANCED FUNCTIONS TRONG PYTHON
=======================================

Bài tập về closures, nested functions, function attributes, partial functions, functools.
"""

# CÂU HỎI 1: Closures
# a) Viết hàm make_multiplier(k) trả về hàm nhân đối số với k (closure)
# b) Tạo m2 = make_multiplier(2), m3 = make_multiplier(3) và kiểm tra

# Code của bạn ở đây:



# CÂU HỎI 2: Nested functions và function attributes
# a) Viết hàm outer đếm số lần inner được gọi, lưu vào thuộc tính inner.calls

# Code của bạn ở đây:



# CÂU HỎI 3: functools.partial
# a) Tạo hàm add(a, b, c) và dùng partial để cố định một số tham số

# Code của bạn ở đây:



# CÂU HỎI 4: functools.lru_cache
# a) Viết fib(n) có dùng lru_cache để tối ưu

# Code của bạn ở đây:



# CÂU HỎI 5: Tổ hợp hàm (function composition)
# a) Viết compose(f, g) trả về hàm h(x) = f(g(x))

# Code của bạn ở đây:



'''
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

from functools import partial, lru_cache

# CÂU HỎI 1:
def make_multiplier(k: int):
    def inner(x: int):
        return x * k
    return inner

m2 = make_multiplier(2)
m3 = make_multiplier(3)
print(m2(10), m3(10))

# CÂU HỎI 2:
def outer():
    calls = {"n": 0}
    def inner():
        calls["n"] += 1
        inner.calls = calls["n"]
        return calls["n"]
    inner.calls = 0
    return inner

f = outer()
print(f(), f(), f(), "- calls:", f.calls)

# CÂU HỎI 3:
def add(a, b, c):
    return a + b + c

add_10 = partial(add, 10)
add_10_5 = partial(add, 10, 5)
print(add_10(1, 2))   # 13
print(add_10_5(3))    # 18

# CÂU HỎI 4:
@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(i) for i in range(10)])

# CÂU HỎI 5:
def compose(f, g):
    def h(x):
        return f(g(x))
    return h

def inc(x):
    return x + 1

def double(x):
    return x * 2

inc_then_double = compose(double, inc)
print(inc_then_double(10))  # (10+1)*2 = 22


# BÀI TẬP NÂNG CAO 1:
# Viết curry(fn) để chuyển một hàm n-arity thành chuỗi hàm nhận từng tham số một.

# BÀI TẬP NÂNG CAO 2:
# Viết factory tạo event handler lưu trạng thái (đếm số sự kiện) bằng closure; cung cấp reset().
'''