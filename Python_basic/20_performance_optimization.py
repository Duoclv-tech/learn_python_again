"""
PHẦN 20: TỐI ƯU HIỆU NĂNG (PERFORMANCE OPTIMIZATION)
====================================================

Bài tập về profiling, Cython (khái niệm), NumPy integration, tối ưu bộ nhớ, độ phức tạp thuật toán.
"""

# CÂU HỎI 1: Profiling code
# a) Dùng time/perf_counter đo thời gian cho hai cách nối chuỗi: + và ''.join
# b) Dùng cProfile để profile một hàm tính toán

# Code của bạn ở đây:



# CÂU HỎI 2: Cython (khái niệm)
# a) Mô tả ngắn cách dùng Cython tăng tốc (pyx, setup.py, cdef types)
# b) Nêu ví dụ tối ưu vòng lặp lớn bằng Cython

# Trả lời của bạn ở đây:



# CÂU HỎI 3: NumPy integration
# a) So sánh tính bình phương 1e6 số bằng list comprehension vs NumPy vectorization
# b) Dùng broadcasting để tính toán ma trận nhanh

# Code của bạn ở đây:



# CÂU HỎI 4: Memory optimization techniques
# a) So sánh bộ nhớ dùng list vs array('i') vs NumPy array dtype nhỏ
# b) Dùng generator thay vì list để xử lý dữ liệu lớn

# Code của bạn ở đây:



# CÂU HỎI 5: Algorithm complexity
# a) Viết các phiên bản tìm kiếm tuyến tính O(n) và nhị phân O(log n)
# b) Phân tích độ phức tạp thời gian và không gian

# Code của bạn ở đây:



"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

import time
import cProfile
import pstats
from io import StringIO

def concat_plus(n=20_000):
    s = ""
    for i in range(n):
        s += str(i)
    return len(s)

def concat_join(n=20_000):
    return len("".join(str(i) for i in range(n)))

t0 = time.perf_counter(); concat_plus(); t1 = time.perf_counter()
t2 = time.perf_counter(); concat_join(); t3 = time.perf_counter()
print("+  :", (t1-t0)*1000, "ms")
print("join:", (t3-t2)*1000, "ms")

def heavy_func(n=300_00):
    total = 0
    for i in range(n):
        total += (i % 7) * (i % 11)
    return total

pr = cProfile.Profile(); pr.enable(); heavy_func(); pr.disable()
s = StringIO(); ps = pstats.Stats(pr, stream=s).sort_stats("cumtime"); ps.print_stats(10)
print(s.getvalue())

# CÂU HỎI 2: Cython
cython_note = """
1) Viết mã trong file .pyx, khai báo kiểu với cdef/ctypedef để giảm overhead Python.
2) Dùng setup.py hoặc pyproject.toml để build extension (setuptools/cythonize).
3) Gọi hàm Cython như module Python bình thường.
Ví dụ: tối ưu vòng lặp for bằng cdef int i; cdef double acc.
"""
print(cython_note)

# CÂU HỎI 3: NumPy
import numpy as np

n = 1_000_000
t0 = time.perf_counter(); a = [i*i for i in range(n)]; t1 = time.perf_counter()
t2 = time.perf_counter(); b = np.arange(n, dtype=np.int64); b = b*b; t3 = time.perf_counter()
print("List comp:", (t1-t0)*1000, "ms; NumPy:", (t3-t2)*1000, "ms")

M = np.random.rand(1000, 1000)
v = np.random.rand(1000)
t0 = time.perf_counter(); r1 = M @ v; t1 = time.perf_counter()
print("Matrix-vector product:", (t1-t0)*1000, "ms")

# CÂU HỎI 4: Memory optimization
import sys
from array import array

lst = list(range(1_000_0))
nparr = np.arange(1_000_0, dtype=np.int32)
arr = array('i', range(1_000_0))
print("list bytes approx:", sys.getsizeof(lst) + len(lst)*sys.getsizeof(0))
print("numpy bytes:", nparr.nbytes)
print("array bytes:", len(arr)*arr.itemsize)

def gen():
    for i in range(10_000_00):
        yield i*i

g = gen()  # không tiêu thụ nhiều bộ nhớ như list
print("Generator created", g)

# CÂU HỎI 5: Algorithm complexity
def linear_search(a, x):
    for i, v in enumerate(a):
        if v == x:
            return i
    return -1

def binary_search(a, x):
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x: return mid
        if a[mid] < x: lo = mid + 1
        else: hi = mid - 1
    return -1

arr_sorted = list(range(0, 1_000_00, 2))
print("linear:", linear_search(arr_sorted, 77776))
print("binary:", binary_search(arr_sorted, 77776))

"""

