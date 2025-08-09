"""
PHẦN 12: ADVANCED OOP TRONG PYTHON
==================================

Bài tập từ cơ bản đến nâng cao về Advanced OOP: Magic methods, Property, Class/Static methods,
Multiple Inheritance, MRO, và Abstract Base Classes.
"""

# CÂU HỎI 1: Magic methods
# a) Tạo class Vector 2D với thuộc tính x, y
# b) Cài đặt __repr__, __str__ để hiển thị đẹp
# c) Cài đặt __len__ trả về độ dài làm tròn (int) của vector (chuẩn Euclid)
# d) Cài đặt __eq__ so sánh bằng theo x và y
# e) Cài đặt __add__ để cộng hai vector

# Code của bạn ở đây:



# CÂU HỎI 2: Property decorators
# a) Tạo class Celsius lưu trữ nhiệt độ theo độ C trong thuộc tính private __celsius
# b) Dùng @property để truy cập celsius, @setter để set với ràng buộc (>= -273.15)
# c) Thêm property fahrenheit chuyển đổi qua lại (C <-> F)

# Code của bạn ở đây:



# CÂU HỎI 3: Class methods và Static methods
# a) Tạo class Employee có các thuộc tính name, salary
# b) Tạo classmethod from_string("name,salary") để khởi tạo nhanh
# c) Tạo staticmethod validate_salary(s) trả về True/False

# Code của bạn ở đây:



# CÂU HỎI 4: Multiple inheritance và MRO
# a) Tạo các class A, B, C(A, B) và in MRO của C
# b) Mỗi class có phương thức greet() ghi log theo tên class, gọi greet() trên C và quan sát MRO

# Code của bạn ở đây:



# CÂU HỎI 5: Abstract Base Classes (ABC)
# a) Tạo ABC Shape có abstract method area()
# b) Tạo Rectangle và Circle kế thừa và cài đặt area()
# c) Tạo hàm print_area(shape) in diện tích một cách đa hình

# Code của bạn ở đây:



"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
import math

class Vector:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"<{self.x}, {self.y}>"

    def __len__(self) -> int:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return int(round(length))

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(repr(v1))
print(str(v1))
print(f"|v1| làm tròn = {len(v1)}")
print(f"v1 == v2? {v1 == v2}")
print(f"v1 + v2 = {v1 + v2}")

# CÂU HỎI 2:
class Celsius:
    ABSOLUTE_ZERO = -273.15

    def __init__(self, celsius: float):
        self.__celsius = None
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self.__celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        value = float(value)
        if value < self.ABSOLUTE_ZERO:
            raise ValueError("Nhiệt độ nhỏ hơn 0 tuyệt đối!")
        self.__celsius = value

    @property
    def fahrenheit(self) -> float:
        return self.__celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self.celsius = (float(value) - 32) * 5 / 9

t = Celsius(25)
print(f"C: {t.celsius}, F: {t.fahrenheit}")
t.fahrenheit = 212
print(f"Sau khi set F=212 -> C: {t.celsius:.2f}")

# CÂU HỎI 3:
class Employee:
    def __init__(self, name: str, salary: float):
        if not Employee.validate_salary(salary):
            raise ValueError("Lương không hợp lệ")
        self.name = name
        self.salary = float(salary)

    @classmethod
    def from_string(cls, raw: str):
        name, salary = [p.strip() for p in raw.split(",", 1)]
        return cls(name, float(salary))

    @staticmethod
    def validate_salary(s) -> bool:
        try:
            return float(s) >= 0
        except Exception:
            return False

e1 = Employee.from_string("Nguyen Van A, 1500")
print(e1.name, e1.salary)
print("Validate -10:", Employee.validate_salary(-10))

# CÂU HỎI 4:
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    def greet(self):
        print("Hello from C ->", end=" ")
        super().greet()

print("MRO của C:", [cls.__name__ for cls in C.mro()])
C().greet()

# CÂU HỎI 5:
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return math.pi * self.r * self.r

def print_area(shape: Shape):
    print(f"Diện tích: {shape.area():.2f}")

print_area(Rectangle(3, 4))
print_area(Circle(2))


# BÀI TẬP NÂNG CAO 1:
# Xây dựng class Matrix hỗ trợ +, -, * (nhân ma trận), ==, repr/str, shape, indexing an toàn
# Gợi ý: lưu dữ liệu trong list[list[float]], kiểm tra kích thước trước khi tính toán


# BÀI TẬP NÂNG CAO 2:
# Thiết kế hệ thống plugin:
# - Tạo ABC Plugin với method run(data)
# - Tạo PluginRegistry (class) để đăng ký plugin qua decorator @register
# - Cho phép liệt kê, khởi tạo và chạy các plugin theo tên



"""
