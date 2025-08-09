"""
PHẦN 18: METACLASSES TRONG PYTHON
=================================

Bài tập về quá trình tạo class, __new__, metaclass tùy biến, và type().
"""

# CÂU HỎI 1: Class creation process
# a) Dùng type để tạo class động: MyDynamic = type('MyDynamic', (object,), {'x': 1, 'hello': lambda self: 'hi'})
# b) Tạo object và gọi phương thức

# Code của bạn ở đây:



# CÂU HỎI 2: __new__ vs __init__
# a) Viết class LogNewInit ghi log khi __new__ và __init__ được gọi

# Code của bạn ở đây:



# CÂU HỎI 3: Metaclass cơ bản
# a) Viết metaclass RequireAttrs bắt buộc class phải có thuộc tính class-level: required = True
# b) Nếu thiếu, raise TypeError khi tạo class

# Code của bạn ở đây:



# CÂU HỎI 4: Metaclass nâng cao - auto register
# a) Viết metaclass AutoRegister tự động đăng ký các subclass vào một registry theo tên class

# Code của bạn ở đây:



'''
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
MyDynamic = type('MyDynamic', (object,), {
    'x': 1,
    'hello': lambda self: 'hi'
})
inst = MyDynamic()
print(inst.x, inst.hello())

# CÂU HỎI 2:
class LogNewInit:
    def __new__(cls, *args, **kwargs):
        print("__new__ của", cls.__name__)
        return super().__new__(cls)

    def __init__(self):
        print("__init__ của", self.__class__.__name__)

LogNewInit()

# CÂU HỎI 3:
class RequireAttrs(type):
    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != 'BaseRequired':
            # Bỏ qua lớp gốc
            if not namespace.get('required', False):
                raise TypeError(f"Class {name} phải định nghĩa 'required = True'")
        return cls

class BaseRequired(metaclass=RequireAttrs):
    required = True

class Implemented(BaseRequired):
    required = True

print("Tạo class Implemented thành công")

# CÂU HỎI 4:
class AutoRegister(type):
    registry = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != 'BaseAuto':
            AutoRegister.registry[name] = cls
        return cls

class BaseAuto(metaclass=AutoRegister):
    pass

class ServiceA(BaseAuto):
    pass

class ServiceB(BaseAuto):
    pass

print("Registry:", AutoRegister.registry)


# BÀI TẬP NÂNG CAO 1:
# Viết Singleton bằng metaclass: nếu đã có instance, trả về instance cũ.

# BÀI TẬP NÂNG CAO 2:
# Viết metaclass kiểm tra lớp phải có các phương thức cụ thể (vd: run, stop). Nếu thiếu -> TypeError.
'''