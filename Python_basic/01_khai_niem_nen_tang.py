"""
PHẦN 1: KHÁI NIỆM NỀN TẢNG PYTHON
=================================

Bài tập từ cơ bản đến nâng cao để luyện tập các khái niệm nền tảng của Python.
"""

# CÂU HỎI 1: Cài đặt Python và môi trường phát triển
# Hãy kiểm tra phiên bản Python đang sử dụng và in ra màn hình
# Gợi ý: Sử dụng module sys

# Code của bạn ở đây:
print(sys.version)
python --version

# CÂU HỎI 2: Cú pháp cơ bản và quy tắc đặt tên
# Hãy sửa các lỗi cú pháp và quy tắc đặt tên trong đoạn code sau:

variable1 = 10
class Python:
    def1 = 5
    my_variable = 20
    print(variable1)

# Code đã sửa:



# CÂU HỎI 3: Comments và docstrings
# Viết một hàm tính diện tích hình chữ nhật với docstring đầy đủ
# (mô tả hàm, tham số, giá trị trả về, ví dụ)

# Code của bạn ở đây:
def cul_square(length, width):
    """
    Tính diện tích hình chữ nhật.
    
    Parameters:
        length (float): Chiều dài của hình chữ nhật
        width (float): Chiều rộng của hình chữ nhật
    
    Returns:
        float: Diện tích của hình chữ nhật
    
    Examples:
        >>> cul_square(5, 3)
        15.0
    """
    return length * width


# CÂU HỎI 4: Indentation (thụt lề) và cấu trúc code
# Sửa lỗi thụt lề trong đoạn code sau:

def check_number(x):
if x > 0:
print("Số dương")
else:
    print("Số không dương")
        print("Kết thúc kiểm tra")

# Code đã sửa:



# BÀI TẬP NÂNG CAO 1:
# Viết một chương trình nhỏ sử dụng cả comments, docstrings và cấu trúc thụt lề đúng
# để tính số Fibonacci thứ n (với n là đầu vào từ người dùng)

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 2:
# Tạo một script Python có thể chạy trực tiếp từ terminal (với shebang line),
# script này sẽ nhận tham số dòng lệnh và hiển thị thông tin về Python environment
# Gợi ý: Sử dụng modules như sys, platform, os

# Code của bạn ở đây:


"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
import sys
print(f"Phiên bản Python: {sys.version}")

# CÂU HỎI 2:
variable1 = 10
class_name = "Python"
def_value = 5
my_variable = 20
print(variable1)

# CÂU HỎI 3:
def tinh_dien_tich_hcn(chieu_dai, chieu_rong):
    '''
    Tính diện tích hình chữ nhật.
    
    Parameters:
        chieu_dai (float): Chiều dài của hình chữ nhật
        chieu_rong (float): Chiều rộng của hình chữ nhật
    
    Returns:
        float: Diện tích của hình chữ nhật
    
    Examples:
        >>> tinh_dien_tich_hcn(5, 3)
        15.0
    '''
    return chieu_dai * chieu_rong

# CÂU HỎI 4:
def check_number(x):
    if x > 0:
        print("Số dương")
    else:
        print("Số không dương")
    print("Kết thúc kiểm tra")

# BÀI TẬP NÂNG CAO 1:
def fibonacci(n):
    '''
    Tính số Fibonacci thứ n.
    
    Parameters:
        n (int): Vị trí của số Fibonacci cần tính (bắt đầu từ 0)
    
    Returns:
        int: Số Fibonacci thứ n
    '''
    # Trường hợp cơ bản
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Tính toán Fibonacci bằng vòng lặp
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Nhận đầu vào từ người dùng
try:
    n = int(input("Nhập số n: "))
    print(f"Số Fibonacci thứ {n} là: {fibonacci(n)}")
except ValueError:
    print("Vui lòng nhập một số nguyên!")

# BÀI TẬP NÂNG CAO 2:
#!/usr/bin/env python3

import sys
import platform
import os

def show_python_info():
    '''Hiển thị thông tin về môi trường Python hiện tại.'''
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Python path: {sys.executable}")
    print(f"Working directory: {os.getcwd()}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("Usage: python script.py [--help]")
        print("Displays information about the Python environment")
    else:
        show_python_info()
"""

