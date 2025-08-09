"""
PHẦN 15: CONTEXT MANAGERS TRONG PYTHON
=====================================

Bài tập về __enter__/__exit__, contextlib, và custom context managers.
"""

# CÂU HỎI 1: __enter__ và __exit__
# a) Viết class Timer làm context manager đo thời gian khối lệnh
# b) Sử dụng Timer để đo thời gian chạy một đoạn code

# Code của bạn ở đây:



# CÂU HỎI 2: contextlib.contextmanager
# a) Viết context manager tạm thời đổi thư mục làm việc (chdir)
# b) Đảm bảo quay lại thư mục cũ kể cả khi có lỗi

# Code của bạn ở đây:



# CÂU HỎI 3: Quản lý tài nguyên
# a) Viết context manager mở file an toàn, tự động đóng
# b) Tạo bản ghi log khi mở/đóng file

# Code của bạn ở đây:



# CÂU HỎI 4: contextlib.suppress
# a) Dùng suppress để bỏ qua FileNotFoundError khi xóa file không tồn tại

# Code của bạn ở đây:



'''
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

import os
import time
from contextlib import contextmanager, suppress

# CÂU HỎI 1:
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = (time.perf_counter() - self.start) * 1000
        print(f"Khối lệnh chạy trong {self.elapsed:.2f} ms")
        # Không nuốt exception
        return False

with Timer():
    total = sum(range(1, 1_000_00))

# CÂU HỎI 2:
@contextmanager
def change_dir(path: str):
    old = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old)

print("Thư mục hiện tại:", os.getcwd())
with change_dir("."):
    print("Trong context:", os.getcwd())
print("Sau context:", os.getcwd())

# CÂU HỎI 3:
@contextmanager
def open_file_safe(path: str, mode: str, encoding: str = "utf-8"):
    print(f"[LOG] Opening {path} mode={mode}")
    f = open(path, mode, encoding=encoding)
    try:
        yield f
    finally:
        f.close()
        print(f"[LOG] Closed {path}")

with open_file_safe("cm_sample.txt", "w") as f:
    f.write("Hello context managers")

# CÂU HỎI 4:
with suppress(FileNotFoundError):
    os.remove("khong_ton_tai.txt")
print("Đã suppress FileNotFoundError nếu có")


# BÀI TẬP NÂNG CAO 1:
# Viết context manager Transaction cho một lớp Database giả lập:
# - __enter__ bắt đầu transaction, __exit__ commit nếu không lỗi, rollback nếu có lỗi.

# BÀI TẬP NÂNG CAO 2:
# Viết context manager tạm thời đặt biến môi trường (os.environ), tự động khôi phục ban đầu khi thoát.
'''