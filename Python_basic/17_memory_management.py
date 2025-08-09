"""
PHẦN 17: QUẢN LÝ BỘ NHỚ (MEMORY MANAGEMENT) TRONG PYTHON
=========================================================

Bài tập về garbage collection, reference counting, memory profiling, del, weakref.
"""

# CÂU HỎI 1: Reference counting
# a) Sử dụng sys.getrefcount để quan sát số tham chiếu của một object

# Code của bạn ở đây:



# CÂU HỎI 2: Garbage collection
# a) Dùng gc để lấy trạng thái GC, bật/tắt, và ép thu gom

# Code của bạn ở đây:



# CÂU HỎI 3: tracemalloc (profiling bộ nhớ)
# a) Dùng tracemalloc để chụp snapshot trước/sau khi tạo list lớn và so sánh

# Code của bạn ở đây:



# CÂU HỎI 4: del và vòng tham chiếu
# a) Tạo hai object tham chiếu chéo nhau, xóa tham chiếu bên ngoài, ép GC và quan sát

# Code của bạn ở đây:



# CÂU HỎI 5: weakref
# a) Dùng weakref để giữ tham chiếu yếu, quan sát đối tượng bị GC khi không còn tham chiếu mạnh

# Code của bạn ở đây:



'''
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

import sys
import gc
import tracemalloc
import weakref

# CÂU HỎI 1:
obj = []
print("Tham chiếu obj ban đầu:", sys.getrefcount(obj))  # Lưu ý: getrefcount tự nó tạo thêm 1 tham chiếu tạm
tmp = obj
print("Sau khi gán tmp=obj:", sys.getrefcount(obj))
del tmp
print("Sau khi del tmp:", sys.getrefcount(obj))

# CÂU HỎI 2:
print("GC enabled?", gc.isenabled())
gc.disable()
print("Sau disable ->", gc.isenabled())
gc.enable()
print("Sau enable  ->", gc.isenabled())
unreachable = gc.collect()
print("Số object không thể reach được GC thu gom:", unreachable)

# CÂU HỎI 3:
tracemalloc.start()
snap1 = tracemalloc.take_snapshot()
big_list = [0] * (10**6)
snap2 = tracemalloc.take_snapshot()
top_stats = snap2.compare_to(snap1, 'lineno')
print("Top thay đổi bộ nhớ:")
for stat in top_stats[:3]:
    print(stat)
tracemalloc.stop()

# CÂU HỎI 4:
class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None
    def __repr__(self):
        return f"Node({self.name})"

a = Node('A')
b = Node('B')
a.ref = b
b.ref = a  # vòng tham chiếu

del a
del b

unreachable = gc.collect()
print("Sau khi del a,b và gc.collect():", unreachable, "object được thu gom")

# CÂU HỎI 5:
class Data:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Data({self.value})"

d = Data(123)
weak_d = weakref.ref(d)
print("Weak ref còn sống?", weak_d() is not None)
del d
gc.collect()
print("Sau khi del strong ref, weak ref còn?", weak_d() is not None)


# BÀI TẬP NÂNG CAO 1:
# Dùng tracemalloc tạo 2 snapshot ở hai thời điểm trong chương trình thực tế, so sánh để phát hiện rò rỉ bộ nhớ.

# BÀI TẬP NÂNG CAO 2:
# Thiết kế ObjectPool đơn giản: acquire/release đối tượng để tái sử dụng thay vì tạo mới liên tục.
'''