"""
PHẦN 14: GENERATORS VÀ ITERATORS TRONG PYTHON
===========================================

Bài tập về iterator protocol, generator functions, generator expressions, và itertools.
"""

# CÂU HỎI 1: Iterator protocol
# a) Tạo class Countdown(n) là một iterator đếm ngược từ n về 1
# b) Cài đặt __iter__ và __next__ đúng chuẩn

# Code của bạn ở đây:



# CÂU HỎI 2: Generator function (yield)
# a) Viết generator fibonacci(limit) sinh dãy Fibonacci <= limit
# b) Viết generator chunks(iterable, size) chia iterables thành các khối size

# Code của bạn ở đây:



# CÂU HỎI 3: Generator expressions
# a) Tạo generator expression bình phương của các số 1..10 và tính tổng
# b) Tạo generator expression lọc số chia hết cho 3 trong 1..100

# Code của bạn ở đây:



# CÂU HỎI 4: itertools module
# a) Dùng itertools.islice để lấy 10 phần tử đầu của một generator vô hạn
# b) Dùng itertools.chain để nối nhiều iterables
# c) Dùng itertools.groupby để nhóm các từ theo độ dài

# Code của bạn ở đây:



'''
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

from itertools import islice, chain, groupby

# CÂU HỎI 1:
class Countdown:
    def __init__(self, n: int):
        self.current = int(n)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print(list(Countdown(5)))

# CÂU HỎI 2:
def fibonacci(limit: int):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

def chunks(iterable, size: int):
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

print(list(fibonacci(50)))
print(list(chunks(range(1, 11), 3)))

# CÂU HỎI 3:
total_squares = sum(x * x for x in range(1, 11))
divisible_by_3 = list(x for x in range(1, 101) if x % 3 == 0)
print("Tổng bình phương 1..10:", total_squares)
print("Số chia hết cho 3 1..100:", divisible_by_3[:10], "...")

# CÂU HỎI 4:
def naturals():
    n = 1
    while True:
        yield n
        n += 1

first_10 = list(islice(naturals(), 10))
print("10 số tự nhiên đầu tiên:", first_10)

combined = list(chain([1, 2], (3, 4), {5, 6}))
print("Nối nhiều iterables:", combined)

words = ["a", "be", "to", "see", "tree", "no", "go", "free"]
words_sorted = sorted(words, key=len)
groups = {k: list(g) for k, g in groupby(words_sorted, key=len)}
print("Nhóm theo độ dài:", groups)


# BÀI TẬP NÂNG CAO 1:
# Xử lý file lớn dạng streaming: viết generator read_lines(path) trả về từng dòng không giữ toàn bộ file
# trong bộ nhớ; viết pipeline: read_lines -> (lọc) -> (chuyển đổi) -> (ghi ra)

# BÀI TẬP NÂNG CAO 2:
# Viết generator window(iterable, size, step=1) tạo các cửa sổ trượt kích thước size, bước step.
'''