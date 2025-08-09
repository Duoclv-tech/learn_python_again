"""
PHẦN 21: ADVANCED BUILT-INS
===========================

Bài tập về __slots__, weakref, descriptor protocol, dataclasses, enum.
"""

# CÂU HỎI 1: __slots__
# a) Tạo class Point với __slots__ = ('x', 'y') và so sánh bộ nhớ với class không dùng slots
# b) Thử gán thuộc tính mới và quan sát lỗi AttributeError

# Code của bạn ở đây:



# CÂU HỎI 2: Weak references
# a) Dùng weakref.WeakValueDictionary để cache object mà không giữ tham chiếu mạnh

# Code của bạn ở đây:



# CÂU HỎI 3: Descriptor protocol
# a) Viết descriptor PositiveNumber để đảm bảo giá trị > 0
# b) Áp dụng vào class Product(price, quantity)

# Code của bạn ở đây:



# CÂU HỎI 4: Data classes
# a) Dùng dataclass để định nghĩa class User(id, name, email) với order=True
# b) Thử frozen=True và quan sát bất biến

# Code của bạn ở đây:



# CÂU HỎI 5: Enum classes
# a) Định nghĩa enum Role {ADMIN, USER, GUEST}
# b) Dùng auto() và gán giá trị tuỳ ý

# Code của bạn ở đây:



"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

import sys
import weakref
from dataclasses import dataclass
from enum import Enum, auto

# CÂU HỎI 1: __slots__
class PointSlots:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x; self.y = y

class PointNoSlots:
    def __init__(self, x, y):
        self.x = x; self.y = y

p1 = PointSlots(1, 2); p2 = PointNoSlots(1, 2)
print("size slots:   ", sys.getsizeof(p1))
print("size no slots:", sys.getsizeof(p2))
# Gán thuộc tính mới -> lỗi
try:
    p1.z = 3
except AttributeError as e:
    print("slots không cho gán thuộc tính mới:", e)

# CÂU HỎI 2: Weak references
class Image:
    def __init__(self, name): self.name = name

cache = weakref.WeakValueDictionary()
img = Image("logo.png")
cache["logo"] = img
print("Trong cache?", "logo" in cache)
del img
print("Sau GC, còn trong cache?", "logo" in cache)

# CÂU HỎI 3: Descriptor
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name)
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Giá trị phải > 0")
        setattr(instance, self.private_name, value)

class Product:
    price = PositiveNumber()
    quantity = PositiveNumber()
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

phone = Product(10_000, 2)
print(phone.price, phone.quantity)

# CÂU HỎI 4: Dataclasses
@dataclass(order=True)
class User:
    id: int
    name: str
    email: str

u1 = User(1, "A", "a@example.com")
u2 = User(2, "B", "b@example.com")
print(u1 < u2)

@dataclass(frozen=True)
class Config:
    host: str
    port: int

cfg = Config("localhost", 5432)
print(cfg)
try:
    cfg.port = 3306
except Exception as e:
    print("frozen dataclass không cho đổi:", e)

# CÂU HỎI 5: Enum
class Role(Enum):
    ADMIN = auto()
    USER = auto()
    GUEST = auto()

print(Role.ADMIN, Role.USER, Role.GUEST)

"""

