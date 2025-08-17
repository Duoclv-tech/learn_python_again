"""
PHẦN 2: KIỂU DỮ LIỆU VÀ BIẾN TRONG PYTHON
=========================================

Bài tập từ cơ bản đến nâng cao để luyện tập về kiểu dữ liệu và biến trong Python.
"""

# CÂU HỎI 1: Numbers (int, float, complex)
# Viết code để thực hiện các phép tính sau và in kết quả:
# a) 5 mũ 3
# b) Căn bậc 2 của 16
# c) Phần nguyên của phép chia 17 cho 3
# d) Phần dư của phép chia 17 cho 3
# e) Tạo một số phức với phần thực là 3 và phần ảo là 4, sau đó tính độ lớn của nó

# Code của bạn ở đây:
5**3
import math
print(f"Căn bậc 2 của 16 = {math.sqrt(16)}")
print(f"Phần nguyên của 17/3 = {17 // 3}")
print(f"Phần dư của 17/3 = {17 % 3}")
z = complex(3, 4)
print(f"Số phức: {z}")
print(f"Độ lớn: {abs(z)}")

# CÂU HỎI 2: Strings và string methods
# Cho chuỗi s = "Python Programming Language"
# a) In ra độ dài của chuỗi => len(3)
# b) Chuyển chuỗi thành chữ hoa => s.upper()
# c) Đếm số lần ký tự 'a' xuất hiện => s.count('a')
# d) Thay thế "Programming" bằng "Coding" => s.replace("Programming", "Coding")
# e) Tách chuỗi thành danh sách các từ => s.split()

s = "Python Programming Language"
# Code của bạn ở đây:
print(f"Độ dài chuỗi: {len(s)}")
print(f"Chuỗi chữ hoa: {s.upper()}")
print(f"Số lần 'a' xuất hiện: {s.count('a')}")
print(f"Chuỗi sau khi thay thế: {s.replace('Programming', 'Coding')}")
print(f"Danh sách các từ: {s.split()}")

# CÂU HỎI 3: Booleans và logical operations
# Viết code để kiểm tra các điều kiện sau và in kết quả:
# a) 5 lớn hơn 3 VÀ 10 chia hết cho 2  => if 5 > 3 and 10 % 2 == 0: print("Điều kiện a đúng")
# b) 7 lớn hơn 10 HOẶC 3 nhỏ hơn 2  => if 7 > 10 or 3 < 2: print("Điều kiện b đúng")
# c) Phủ định của (5 bằng 5)  => if not (5 == 5): print("Điều kiện c đúng")
# d) 7 không bằng 7  => if 7 != 7: print("Điều kiện d đúng")

# Code của bạn ở đây:



# CÂU HỎI 4: Variables và assignment
# a) Gán giá trị 10 cho biến x và 20 cho biến y, sau đó hoán đổi giá trị của chúng =>  x = 10 y =20  => x, y = y, x
# b) Gán cùng giá trị 100 cho 3 biến a, b, c trong một dòng code => a = b = c = 100
# c) Gán các giá trị 5, 10, 15 cho ba biến d, e, f trong một dòng code => d,e,f = 5, 10, 15

# Code của bạn ở đây:



# CÂU HỎI 5: Type conversion và type checking
# a) Chuyển số 7.8 thành số nguyên và in kết quả => int(7.8)
# b) Chuyển số nguyên 42 thành chuỗi và nối với chuỗi " là câu trả lời"  => f"{42} là câu trả lời"
# c) Kiểm tra kiểu dữ liệu của biến x sau khi gán x = 5.0 => type(x)
# d) Chuyển chuỗi "3.14" thành số thực và cộng với 2.0 => float(3.14) + 2.0

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 1:
# Viết chương trình tính chỉ số BMI (Body Mass Index)
# BMI = cân nặng (kg) / (chiều cao (m))^2
# Chương trình nhận đầu vào là cân nặng (kg) và chiều cao (cm)
# Kết quả làm tròn đến 2 chữ số thập phân và phân loại theo:
# - Dưới 18.5: Thiếu cân
# - 18.5 - 24.9: Bình thường
# - 25.0 - 29.9: Thừa cân
# - Trên 30.0: Béo phì

# Code của bạn ở đây:

def cul_IBM():
    x, y = input("nhập chiều cao và cân nặng").split()
    x = float(x) / 100  # Chuyển từ cm sang m
    y = float(y)
    if x <= 0 or y <= 0:
        print("Chiều cao và cân nặng phải là số dương!")
        return
    bmi = y / (x ** 2)
    bmi_rounded = round(bmi, 2)
    print(f"Chỉ số BMI của bạn là: {bmi_rounded}")
    if bmi < 18.5:
        print("Phân loại: Thiếu cân")
    elif 18.5 <= bmi < 25.0:
        print("Phân loại: Bình thường")
    elif 25.0 <= bmi < 30.0:
        print("Phân loại: Thừa cân")


# BÀI TẬP NÂNG CAO 2:
# Viết chương trình xử lý chuỗi DNA (chỉ chứa các ký tự A, T, G, C)
# Chương trình nhận một chuỗi DNA và thực hiện:
# a) Kiểm tra tính hợp lệ (chỉ chứa A, T, G, C)
# b) Đếm số lượng từng loại nucleotide (A, T, G, C)
# c) Tính tỷ lệ GC-content (tỷ lệ G và C trong chuỗi)
# d) Tạo chuỗi bổ sung (A->T, T->A, G->C, C->G)

# Code của bạn ở đây:


"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
# a) 5 mũ 3
print(f"5 mũ 3 = {5 ** 3}")

# b) Căn bậc 2 của 16
import math
print(f"Căn bậc 2 của 16 = {math.sqrt(16)}")

# c) Phần nguyên của phép chia 17 cho 3
print(f"Phần nguyên của 17/3 = {17 // 3}")

# d) Phần dư của phép chia 17 cho 3
print(f"Phần dư của 17/3 = {17 % 3}")

# e) Tạo một số phức với phần thực là 3 và phần ảo là 4, sau đó tính độ lớn của nó
z = complex(3, 4)
print(f"Số phức: {z}")
print(f"Độ lớn: {abs(z)}")

# CÂU HỎI 2:
s = "Python Programming Language"

# a) In ra độ dài của chuỗi
print(f"Độ dài chuỗi: {len(s)}")

# b) Chuyển chuỗi thành chữ hoa
print(f"Chuỗi chữ hoa: {s.upper()}")

# c) Đếm số lần ký tự 'a' xuất hiện
print(f"Số lần 'a' xuất hiện: {s.count('a')}")

# d) Thay thế "Programming" bằng "Coding"
print(f"Chuỗi sau khi thay thế: {s.replace('Programming', 'Coding')}")

# e) Tách chuỗi thành danh sách các từ
print(f"Danh sách các từ: {s.split()}")

# CÂU HỎI 3:
# a) 5 lớn hơn 3 VÀ 10 chia hết cho 2
print(f"5 > 3 và 10 chia hết cho 2: {5 > 3 and 10 % 2 == 0}")

# b) 7 lớn hơn 10 HOẶC 3 nhỏ hơn 2
print(f"7 > 10 hoặc 3 < 2: {7 > 10 or 3 < 2}")

# c) Phủ định của (5 bằng 5)
print(f"Phủ định của (5 == 5): {not (5 == 5)}")

# d) 7 không bằng 7
print(f"7 != 7: {7 != 7}")

# CÂU HỎI 4:
# a) Gán giá trị 10 cho biến x và 20 cho biến y, sau đó hoán đổi giá trị của chúng
x = 10
y = 20
print(f"Trước khi hoán đổi: x = {x}, y = {y}")
x, y = y, x
print(f"Sau khi hoán đổi: x = {x}, y = {y}")

# b) Gán cùng giá trị 100 cho 3 biến a, b, c trong một dòng code
a = b = c = 100
print(f"a = {a}, b = {b}, c = {c}")

# c) Gán các giá trị 5, 10, 15 cho ba biến d, e, f trong một dòng code
d, e, f = 5, 10, 15
print(f"d = {d}, e = {e}, f = {f}")

# CÂU HỎI 5:
# a) Chuyển số 7.8 thành số nguyên và in kết quả
print(f"int(7.8) = {int(7.8)}")

# b) Chuyển số nguyên 42 thành chuỗi và nối với chuỗi " là câu trả lời"
print(f"{str(42)} là câu trả lời")

# c) Kiểm tra kiểu dữ liệu của biến x sau khi gán x = 5.0
x = 5.0
print(f"Kiểu dữ liệu của x = 5.0 là: {type(x)}")

# d) Chuyển chuỗi "3.14" thành số thực và cộng với 2.0
print(f"float('3.14') + 2.0 = {float('3.14') + 2.0}")

# BÀI TẬP NÂNG CAO 1:
def tinh_bmi():
    try:
        can_nang = float(input("Nhập cân nặng (kg): "))
        chieu_cao = float(input("Nhập chiều cao (cm): ")) / 100  # Chuyển từ cm sang m
        
        if can_nang <= 0 or chieu_cao <= 0:
            print("Cân nặng và chiều cao phải là số dương!")
            return
        
        bmi = can_nang / (chieu_cao ** 2)
        bmi_rounded = round(bmi, 2)
        
        print(f"Chỉ số BMI của bạn là: {bmi_rounded}")
        
        if bmi < 18.5:
            print("Phân loại: Thiếu cân")
        elif 18.5 <= bmi < 25.0:
            print("Phân loại: Bình thường")
        elif 25.0 <= bmi < 30.0:
            print("Phân loại: Thừa cân")
        else:
            print("Phân loại: Béo phì")
            
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")

# Chạy chương trình tính BMI
# tinh_bmi()

# BÀI TẬP NÂNG CAO 2:
def xu_ly_chuoi_dna(chuoi_dna):
    # a) Kiểm tra tính hợp lệ
    chuoi_dna = chuoi_dna.upper()
    nucleotides_hop_le = set("ATGC")
    
    if not all(nucleotide in nucleotides_hop_le for nucleotide in chuoi_dna):
        print("Chuỗi DNA không hợp lệ! Chỉ chấp nhận các ký tự A, T, G, C.")
        return
    
    # b) Đếm số lượng từng loại nucleotide
    count_a = chuoi_dna.count("A")
    count_t = chuoi_dna.count("T")
    count_g = chuoi_dna.count("G")
    count_c = chuoi_dna.count("C")
    
    print(f"Số lượng A: {count_a}")
    print(f"Số lượng T: {count_t}")
    print(f"Số lượng G: {count_g}")
    print(f"Số lượng C: {count_c}")
    
    # c) Tính tỷ lệ GC-content
    tong_do_dai = len(chuoi_dna)
    gc_content = (count_g + count_c) / tong_do_dai * 100 if tong_do_dai > 0 else 0
    print(f"GC-content: {gc_content:.2f}%")
    
    # d) Tạo chuỗi bổ sung
    bang_bo_sung = str.maketrans("ATGC", "TACG")
    chuoi_bo_sung = chuoi_dna.translate(bang_bo_sung)
    print(f"Chuỗi bổ sung: {chuoi_bo_sung}")

# Chạy chương trình xử lý chuỗi DNA
# chuoi_dna = input("Nhập chuỗi DNA: ")
# xu_ly_chuoi_dna(chuoi_dna)
"""

