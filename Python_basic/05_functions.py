"""
PHẦN 5: FUNCTIONS TRONG PYTHON
============================

Bài tập từ cơ bản đến nâng cao để luyện tập về functions trong Python.
"""

# CÂU HỎI 1: Defining functions (def)
# a) Viết hàm tính tổng của hai số
# b) Viết hàm kiểm tra một số có phải số chẵn không
# c) Viết hàm in ra bảng cửu chương của một số

# Code của bạn ở đây:



# CÂU HỎI 2: Parameters và arguments
# a) Viết hàm chào hỏi với tham số mặc định
# b) Viết hàm tính diện tích hình chữ nhật với 2 tham số
# c) Viết hàm nhận vào một list và một giá trị, trả về số lần giá trị đó xuất hiện trong list

# Code của bạn ở đây:



# CÂU HỎI 3: Return statements
# a) Viết hàm trả về giá trị lớn nhất trong 3 số
# b) Viết hàm kiểm tra một chuỗi có phải là palindrome không (đọc xuôi ngược đều giống nhau)
# c) Viết hàm trả về cả phần nguyên và phần dư của phép chia hai số

# Code của bạn ở đây:



# CÂU HỎI 4: Local vs global scope
# a) Viết một chương trình minh họa sự khác biệt giữa biến local và global
# b) Viết hàm thay đổi giá trị của biến global
# c) Viết hàm có biến local cùng tên với biến global và giải thích kết quả

# Code của bạn ở đây:



# CÂU HỎI 5: Lambda functions
# a) Viết lambda function tính bình phương của một số
# b) Sử dụng lambda với hàm map() để bình phương các số trong một list
# c) Sử dụng lambda với hàm filter() để lọc các số chẵn trong một list
# d) Sử dụng lambda với hàm sorted() để sắp xếp một list các tuples theo phần tử thứ hai

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 1:
# Viết hàm đệ quy tính giai thừa của một số
# Viết hàm đệ quy tính số Fibonacci thứ n
# So sánh hiệu suất của phiên bản đệ quy và phiên bản vòng lặp của hai hàm trên

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 2:
# Viết một decorator để đo thời gian thực thi của một hàm
# Áp dụng decorator này cho các hàm tính giai thừa và Fibonacci ở bài trước
# In ra thời gian thực thi của mỗi hàm

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 3:
# Viết hàm nhận vào một số nguyên dương n và trả về tất cả các số nguyên tố nhỏ hơn hoặc bằng n
# Viết hàm kiểm tra xem một số có phải là số hoàn hảo không (số hoàn hảo là số bằng tổng các ước số dương của nó, không kể chính nó)
# Viết hàm tìm ước chung lớn nhất và bội chung nhỏ nhất của hai số

# Code của bạn ở đây:


"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
# a) Hàm tính tổng hai số
def tinh_tong(a, b):
    return a + b

print(f"Tổng của 5 và 7 là: {tinh_tong(5, 7)}")

# b) Hàm kiểm tra số chẵn
def la_so_chan(n):
    return n % 2 == 0

print(f"15 là số chẵn? {la_so_chan(15)}")
print(f"20 là số chẵn? {la_so_chan(20)}")

# c) Hàm in bảng cửu chương
def in_bang_cuu_chuong(n):
    print(f"Bảng cửu chương {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

in_bang_cuu_chuong(7)

# CÂU HỎI 2:
# a) Hàm chào hỏi với tham số mặc định
def chao_hoi(ten="bạn"):
    return f"Xin chào, {ten}!"

print(chao_hoi())
print(chao_hoi("Nam"))

# b) Hàm tính diện tích hình chữ nhật
def dien_tich_hcn(chieu_dai, chieu_rong):
    return chieu_dai * chieu_rong

print(f"Diện tích hình chữ nhật 5x3 là: {dien_tich_hcn(5, 3)}")

# c) Hàm đếm số lần xuất hiện
def dem_xuat_hien(danh_sach, gia_tri):
    return danh_sach.count(gia_tri)

my_list = [1, 2, 3, 2, 4, 2, 5]
print(f"Số 2 xuất hiện {dem_xuat_hien(my_list, 2)} lần trong list")

# CÂU HỎI 3:
# a) Hàm trả về giá trị lớn nhất trong 3 số
def max_ba_so(a, b, c):
    return max(a, b, c)

print(f"Số lớn nhất trong 3 số 10, 25, 15 là: {max_ba_so(10, 25, 15)}")

# b) Hàm kiểm tra palindrome
def la_palindrome(chuoi):
    # Loại bỏ khoảng trắng và chuyển về chữ thường
    chuoi = chuoi.lower().replace(" ", "")
    return chuoi == chuoi[::-1]

print(f"'radar' là palindrome? {la_palindrome('radar')}")
print(f"'hello' là palindrome? {la_palindrome('hello')}")
print(f"'A man a plan a canal Panama' là palindrome? {la_palindrome('A man a plan a canal Panama')}")

# c) Hàm trả về phần nguyên và phần dư
def chia_lay_nguyen_du(a, b):
    if b == 0:
        return None  # Tránh chia cho 0
    nguyen = a // b
    du = a % b
    return (nguyen, du)

ket_qua = chia_lay_nguyen_du(17, 5)
if ket_qua:
    print(f"17 chia 5 được {ket_qua[0]} dư {ket_qua[1]}")

# CÂU HỎI 4:
# a) Minh họa sự khác biệt giữa biến local và global
x = 10  # Biến global

def demo_scope():
    y = 5  # Biến local
    print(f"Trong hàm: x = {x}, y = {y}")  # Có thể truy cập cả x và y

demo_scope()
print(f"Ngoài hàm: x = {x}")  # Có thể truy cập x
try:
    print(f"Ngoài hàm: y = {y}")  # Không thể truy cập y
except NameError as e:
    print(f"Lỗi: {e}")

# b) Hàm thay đổi giá trị của biến global
count = 0

def tang_count():
    global count
    count += 1
    return count

print(f"Count ban đầu: {count}")
tang_count()
tang_count()
print(f"Count sau khi gọi hàm 2 lần: {count}")

# c) Hàm có biến local cùng tên với biến global
message = "Global message"

def print_message():
    message = "Local message"  # Biến local che khuất biến global
    print(f"Trong hàm: {message}")

print(f"Trước khi gọi hàm: {message}")
print_message()
print(f"Sau khi gọi hàm: {message}")  # Biến global không bị thay đổi

# CÂU HỎI 5:
# a) Lambda function tính bình phương
binh_phuong = lambda x: x**2
print(f"Bình phương của 7: {binh_phuong(7)}")

# b) Lambda với map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(f"Bình phương của {numbers}: {squares}")

# c) Lambda với filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Các số chẵn trong {numbers}: {even_numbers}")

# d) Lambda với sorted()
students = [("Nam", 85), ("Lan", 92), ("Minh", 78), ("Hoa", 95)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print("Danh sách học sinh sắp xếp theo điểm (cao đến thấp):")
for student in sorted_by_score:
    print(f"{student[0]}: {student[1]}")

# BÀI TẬP NÂNG CAO 1:
import time

# Hàm đệ quy tính giai thừa
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Hàm vòng lặp tính giai thừa
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Hàm đệ quy tính Fibonacci
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Hàm vòng lặp tính Fibonacci
def fibonacci_loop(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# So sánh hiệu suất
def compare_performance(func1, func2, n, name):
    # Đo thời gian cho hàm đệ quy
    start = time.time()
    result1 = func1(n)
    end = time.time()
    time1 = end - start
    
    # Đo thời gian cho hàm vòng lặp
    start = time.time()
    result2 = func2(n)
    end = time.time()
    time2 = end - start
    
    print(f"\nSo sánh hiệu suất tính {name}({n}):")
    print(f"Kết quả: {result1}")
    print(f"Đệ quy: {time1:.6f} giây")
    print(f"Vòng lặp: {time2:.6f} giây")
    print(f"Vòng lặp nhanh hơn {time1/time2 if time2 > 0 else 'vô cùng'} lần")

# So sánh hiệu suất cho giai thừa
compare_performance(factorial_recursive, factorial_loop, 20, "Giai thừa")

# So sánh hiệu suất cho Fibonacci
# Lưu ý: với n lớn, hàm đệ quy Fibonacci sẽ rất chậm
compare_performance(fibonacci_recursive, fibonacci_loop, 30, "Fibonacci")

# BÀI TẬP NÂNG CAO 2:
import time
import functools

# Decorator đo thời gian thực thi
def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Thời gian thực thi {func.__name__}: {end_time - start_time:.6f} giây")
        return result
    return wrapper

# Áp dụng decorator cho các hàm
@measure_time
def factorial_recursive_measured(n):
    if n <= 1:
        return 1
    return n * factorial_recursive_measured(n - 1)

@measure_time
def factorial_loop_measured(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@measure_time
def fibonacci_recursive_measured(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive_measured(n - 1) + fibonacci_recursive_measured(n - 2)

@measure_time
def fibonacci_loop_measured(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Thực thi và đo thời gian
print("\nĐo thời gian thực thi:")
factorial_recursive_measured(20)
factorial_loop_measured(20)

# Với Fibonacci, n=30 có thể quá lớn cho phiên bản đệ quy
fibonacci_recursive_measured(20)  # Giảm n xuống để tránh chờ quá lâu
fibonacci_loop_measured(30)

# BÀI TẬP NÂNG CAO 3:
import math

# Hàm trả về tất cả các số nguyên tố nhỏ hơn hoặc bằng n
def find_primes(n):
    """
    Tìm tất cả các số nguyên tố nhỏ hơn hoặc bằng n sử dụng Sieve of Eratosthenes
    """
    if n < 2:
        return []
    
    # Khởi tạo mảng đánh dấu
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Sàng Eratosthenes
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    # Tạo danh sách kết quả
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

# Hàm kiểm tra số hoàn hảo
def is_perfect_number(n):
    """
    Kiểm tra xem n có phải là số hoàn hảo không
    Số hoàn hảo là số bằng tổng các ước số dương của nó (không kể chính nó)
    """
    if n <= 1:
        return False
    
    # Tìm tổng các ước số
    sum_of_divisors = 1  # Bắt đầu với 1 vì 1 luôn là ước số
    
    # Chỉ cần kiểm tra đến căn bậc hai của n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_of_divisors += i
            # Nếu i khác n/i (không phải căn bậc hai của n), thêm n/i
            if i != n // i:
                sum_of_divisors += n // i
    
    return sum_of_divisors == n

# Hàm tìm ước chung lớn nhất (UCLN)
def gcd(a, b):
    """
    Tìm ước chung lớn nhất của a và b sử dụng thuật toán Euclid
    """
    while b:
        a, b = b, a % b
    return a

# Hàm tìm bội chung nhỏ nhất (BCNN)
def lcm(a, b):
    """
    Tìm bội chung nhỏ nhất của a và b
    BCNN(a, b) = (a * b) / UCLN(a, b)
    """
    return a * b // gcd(a, b)

# Kiểm tra các hàm
print("\nCác số nguyên tố nhỏ hơn hoặc bằng 50:")
print(find_primes(50))

print("\nKiểm tra số hoàn hảo:")
for i in range(1, 10000):
    if is_perfect_number(i):
        print(f"{i} là số hoàn hảo")

print("\nTìm UCLN và BCNN:")
a, b = 48, 18
print(f"UCLN({a}, {b}) = {gcd(a, b)}")
print(f"BCNN({a}, {b}) = {lcm(a, b)}")
"""

