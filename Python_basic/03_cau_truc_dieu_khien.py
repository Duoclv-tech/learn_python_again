"""
PHẦN 3: CẤU TRÚC ĐIỀU KHIỂN TRONG PYTHON
=======================================

Bài tập từ cơ bản đến nâng cao để luyện tập về cấu trúc điều khiển trong Python.
"""

# CÂU HỎI 1: Conditional statements (if, elif, else)
# Viết chương trình nhận vào một số nguyên và phân loại:
# - Số âm
# - Số 0
# - Số dương chẵn
# - Số dương lẻ

# Code của bạn ở đây:



# CÂU HỎI 2: Loops (for)
# a) Viết vòng lặp in ra bảng cửu chương của 5 (từ 5x1 đến 5x10)
# b) Viết vòng lặp tính tổng các số từ 1 đến 100

# Code của bạn ở đây:



# CÂU HỎI 3: Loops (while)
# a) Viết vòng lặp while để tìm số Fibonacci thứ 10
# b) Viết vòng lặp while để đoán số (số bí mật là 42, 
#    chương trình sẽ hỏi người dùng đến khi nào đoán đúng)

# Code của bạn ở đây:



# CÂU HỎI 4: Break, continue, pass
# a) Viết vòng lặp in các số từ 1 đến 20, nhưng bỏ qua các số chia hết cho 3
# b) Viết vòng lặp in các số từ 1, dừng lại khi gặp số chia hết cho cả 5 và 7

# Code của bạn ở đây:



# CÂU HỎI 5: Range function
# a) Sử dụng range để tạo list chứa các số chẵn từ 2 đến 20
# b) Sử dụng range để tạo list chứa các số từ 10 đến 1 (đếm ngược)
# c) Sử dụng range để tạo list chứa các số chia hết cho 3 từ 3 đến 30

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 1:
# Viết chương trình kiểm tra số nguyên tố:
# a) Viết hàm is_prime(n) để kiểm tra xem n có phải số nguyên tố không
# b) In ra tất cả các số nguyên tố từ 1 đến 100

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 2:
# Viết chương trình mô phỏng máy ATM với các chức năng:
# - Kiểm tra số dư
# - Rút tiền (kiểm tra số dư đủ không, số tiền rút phải là bội số của 50.000)
# - Nạp tiền
# - Thoát
# Sử dụng vòng lặp để hiển thị menu và xử lý lựa chọn của người dùng

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 3:
# Viết chương trình tìm tất cả các cặp số Pythagorean (a, b, c) thỏa mãn:
# a^2 + b^2 = c^2 với a, b, c là các số nguyên dương và a < b < c <= 100

# Code của bạn ở đây:


"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
def phan_loai_so(n):
    if n < 0:
        print(f"{n} là số âm")
    elif n == 0:
        print("Số 0")
    elif n % 2 == 0:
        print(f"{n} là số dương chẵn")
    else:
        print(f"{n} là số dương lẻ")

# Kiểm tra với một số ví dụ
for so in [-5, 0, 6, 9]:
    phan_loai_so(so)

# CÂU HỎI 2:
# a) Bảng cửu chương của 5
print("Bảng cửu chương của 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# b) Tổng các số từ 1 đến 100
tong = 0
for i in range(1, 101):
    tong += i
print(f"Tổng các số từ 1 đến 100: {tong}")

# CÂU HỎI 3:
# a) Số Fibonacci thứ 10
a, b = 0, 1
count = 0
while count < 10:
    a, b = b, a + b
    count += 1
print(f"Số Fibonacci thứ 10: {a}")

# b) Đoán số
'''
so_bi_mat = 42
while True:
    try:
        doan = int(input("Hãy đoán số (1-100): "))
        if doan < so_bi_mat:
            print("Số bí mật lớn hơn!")
        elif doan > so_bi_mat:
            print("Số bí mật nhỏ hơn!")
        else:
            print("Chúc mừng! Bạn đã đoán đúng.")
            break
    except ValueError:
        print("Vui lòng nhập một số nguyên!")
'''

# CÂU HỎI 4:
# a) In các số từ 1 đến 20, bỏ qua các số chia hết cho 3
print("Các số từ 1 đến 20 không chia hết cho 3:")
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# b) In các số từ 1, dừng khi gặp số chia hết cho cả 5 và 7
print("Các số từ 1, dừng khi gặp số chia hết cho cả 5 và 7:")
for i in range(1, 101):  # Giới hạn trên để tránh vòng lặp vô hạn
    print(i, end=" ")
    if i % 5 == 0 and i % 7 == 0:
        print(f"\nDừng tại {i} vì chia hết cho cả 5 và 7")
        break

# CÂU HỎI 5:
# a) List chứa các số chẵn từ 2 đến 20
so_chan = list(range(2, 21, 2))
print(f"Các số chẵn từ 2 đến 20: {so_chan}")

# b) List chứa các số từ 10 đến 1 (đếm ngược)
dem_nguoc = list(range(10, 0, -1))
print(f"Đếm ngược từ 10 đến 1: {dem_nguoc}")

# c) List chứa các số chia hết cho 3 từ 3 đến 30
chia_het_cho_3 = list(range(3, 31, 3))
print(f"Các số chia hết cho 3 từ 3 đến 30: {chia_het_cho_3}")

# BÀI TẬP NÂNG CAO 1:
def is_prime(n):
    """Kiểm tra số nguyên tố"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# In ra các số nguyên tố từ 1 đến 100
print("Các số nguyên tố từ 1 đến 100:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")
print()

# BÀI TẬP NÂNG CAO 2:
def may_atm():
    so_du = 1000000  # Giả sử số dư ban đầu là 1.000.000 VND
    
    while True:
        print("\n===== CHÀO MỪNG ĐẾN VỚI MÁY ATM =====")
        print("1. Kiểm tra số dư")
        print("2. Rút tiền")
        print("3. Nạp tiền")
        print("4. Thoát")
        
        try:
            lua_chon = int(input("Vui lòng chọn giao dịch (1-4): "))
            
            if lua_chon == 1:
                print(f"Số dư hiện tại của bạn là: {so_du:,} VND")
                
            elif lua_chon == 2:
                so_tien_rut = int(input("Nhập số tiền muốn rút (bội số của 50.000 VND): "))
                
                if so_tien_rut % 50000 != 0:
                    print("Số tiền rút phải là bội số của 50.000 VND!")
                elif so_tien_rut > so_du:
                    print("Số dư không đủ để thực hiện giao dịch này!")
                else:
                    so_du -= so_tien_rut
                    print(f"Rút thành công {so_tien_rut:,} VND")
                    print(f"Số dư còn lại: {so_du:,} VND")
                    
            elif lua_chon == 3:
                so_tien_nap = int(input("Nhập số tiền muốn nạp: "))
                
                if so_tien_nap <= 0:
                    print("Số tiền nạp phải là số dương!")
                else:
                    so_du += so_tien_nap
                    print(f"Nạp thành công {so_tien_nap:,} VND")
                    print(f"Số dư hiện tại: {so_du:,} VND")
                    
            elif lua_chon == 4:
                print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
                break
                
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1-4.")
                
        except ValueError:
            print("Vui lòng nhập số nguyên!")

# Chạy chương trình ATM
# may_atm()

# BÀI TẬP NÂNG CAO 3:
def tim_bo_ba_pythagorean():
    print("Các bộ ba Pythagorean (a, b, c) thỏa mãn a^2 + b^2 = c^2 và a < b < c <= 100:")
    count = 0
    
    for c in range(3, 101):
        for b in range(2, c):
            for a in range(1, b):
                if a*a + b*b == c*c:
                    print(f"({a}, {b}, {c})")
                    count += 1
    
    print(f"Tổng cộng có {count} bộ ba Pythagorean.")

# Chạy chương trình tìm bộ ba Pythagorean
# tim_bo_ba_pythagorean()
"""

