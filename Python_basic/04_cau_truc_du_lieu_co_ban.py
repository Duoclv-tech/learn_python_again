"""
PHẦN 4: CẤU TRÚC DỮ LIỆU CƠ BẢN TRONG PYTHON
=========================================

Bài tập từ cơ bản đến nâng cao để luyện tập về cấu trúc dữ liệu cơ bản trong Python.
"""

# CÂU HỎI 1: Lists và list methods
# a) Tạo một list chứa tên các tháng trong năm
# b) In ra phần tử thứ 3 và phần tử cuối cùng của list
# c) Thêm một phần tử mới vào cuối list
# d) Chèn một phần tử mới vào vị trí thứ 2
# e) Xóa phần tử có giá trị "February" khỏi list
# f) Sắp xếp list theo thứ tự bảng chữ cái
# g) Đảo ngược thứ tự các phần tử trong list

# Code của bạn ở đây:



# CÂU HỎI 2: Tuples và immutability
# a) Tạo một tuple chứa thông tin cá nhân (tên, tuổi, quê quán)
# b) Thử thay đổi giá trị của một phần tử trong tuple và giải thích kết quả
# c) Tạo một list chứa 3 tuples, mỗi tuple chứa thông tin của một sinh viên
# d) Truy cập thông tin tuổi của sinh viên thứ 2

# Code của bạn ở đây:



# CÂU HỎI 3: Dictionaries và key-value pairs
# a) Tạo một dictionary chứa thông tin về một quyển sách (tên, tác giả, năm xuất bản)
# b) Thêm một cặp key-value mới vào dictionary (số trang)
# c) Sửa giá trị của key "năm xuất bản"
# d) Xóa thông tin về tác giả
# e) Kiểm tra xem key "nhà xuất bản" có tồn tại trong dictionary không
# f) In ra tất cả các keys và values của dictionary

# Code của bạn ở đây:



# CÂU HỎI 4: Sets và set operations
# a) Tạo hai sets: một set chứa các số chẵn từ 0-10 và một set chứa các số từ 0-10 chia hết cho 3
# b) Tìm hợp của hai sets
# c) Tìm giao của hai sets
# d) Tìm hiệu của set chẵn trừ set chia hết cho 3
# e) Kiểm tra xem set chẵn có phải là tập con của set [0, 2, 4, 6, 8, 10, 12, 14] không

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 1:
# Viết chương trình quản lý danh sách sinh viên với các chức năng:
# a) Thêm sinh viên mới (ID, tên, điểm trung bình)
# b) Tìm kiếm sinh viên theo ID
# c) Cập nhật thông tin sinh viên
# d) Xóa sinh viên
# e) Hiển thị danh sách sinh viên theo thứ tự điểm giảm dần
# Sử dụng list chứa các dictionaries để lưu trữ thông tin

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 2:
# Viết chương trình đếm tần suất xuất hiện của các từ trong một văn bản
# a) Đọc văn bản từ người dùng
# b) Chuyển văn bản thành chữ thường và loại bỏ dấu câu
# c) Tách văn bản thành các từ
# d) Đếm số lần xuất hiện của mỗi từ
# e) Hiển thị 5 từ xuất hiện nhiều nhất
# Sử dụng dictionary để lưu trữ tần suất

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 3:
# Viết chương trình mô phỏng một bộ từ điển Anh-Việt đơn giản với các chức năng:
# a) Thêm từ mới (từ tiếng Anh, nghĩa tiếng Việt, ví dụ)
# b) Tìm kiếm từ
# c) Cập nhật nghĩa của từ
# d) Xóa từ
# e) Hiển thị toàn bộ từ điển theo thứ tự bảng chữ cái
# f) Lưu từ điển vào file và đọc từ điển từ file
# Sử dụng dictionary để lưu trữ từ điển

# Code của bạn ở đây:


"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
# a) Tạo list chứa tên các tháng
thang = ["January", "February", "March", "April", "May", "June", 
         "July", "August", "September", "October", "November", "December"]

# b) In phần tử thứ 3 và cuối cùng
print(f"Phần tử thứ 3: {thang[2]}")
print(f"Phần tử cuối cùng: {thang[-1]}")

# c) Thêm phần tử mới vào cuối
thang.append("New Month")
print(f"Sau khi thêm phần tử mới: {thang}")

# d) Chèn phần tử mới vào vị trí thứ 2
thang.insert(1, "Extra Month")
print(f"Sau khi chèn phần tử mới: {thang}")

# e) Xóa phần tử "February"
if "February" in thang:
    thang.remove("February")
print(f"Sau khi xóa February: {thang}")

# f) Sắp xếp list
thang.sort()
print(f"Sau khi sắp xếp: {thang}")

# g) Đảo ngược list
thang.reverse()
print(f"Sau khi đảo ngược: {thang}")

# CÂU HỎI 2:
# a) Tạo tuple chứa thông tin cá nhân
thong_tin = ("Nguyễn Văn A", 25, "Hà Nội")
print(f"Thông tin cá nhân: {thong_tin}")

# b) Thử thay đổi giá trị trong tuple
try:
    thong_tin[1] = 26
except TypeError as e:
    print(f"Lỗi: {e}")
    print("Giải thích: Tuple là immutable, không thể thay đổi giá trị của phần tử sau khi đã tạo.")

# c) Tạo list chứa 3 tuples
sinh_vien = [
    ("Nguyễn Văn A", 20, "CNTT"),
    ("Trần Thị B", 21, "Kinh tế"),
    ("Lê Văn C", 19, "Ngoại ngữ")
]
print(f"Danh sách sinh viên: {sinh_vien}")

# d) Truy cập tuổi của sinh viên thứ 2
print(f"Tuổi của sinh viên thứ 2: {sinh_vien[1][1]}")

# CÂU HỎI 3:
# a) Tạo dictionary chứa thông tin sách
sach = {
    "tên": "Python cơ bản",
    "tác giả": "Nguyễn Văn A",
    "năm xuất bản": 2020
}
print(f"Thông tin sách: {sach}")

# b) Thêm cặp key-value mới
sach["số trang"] = 300
print(f"Sau khi thêm số trang: {sach}")

# c) Sửa giá trị
sach["năm xuất bản"] = 2021
print(f"Sau khi sửa năm xuất bản: {sach}")

# d) Xóa thông tin về tác giả
del sach["tác giả"]
print(f"Sau khi xóa tác giả: {sach}")

# e) Kiểm tra key "nhà xuất bản"
if "nhà xuất bản" in sach:
    print("Key 'nhà xuất bản' tồn tại trong dictionary")
else:
    print("Key 'nhà xuất bản' không tồn tại trong dictionary")

# f) In ra tất cả keys và values
print("Tất cả keys:")
for key in sach.keys():
    print(key)

print("Tất cả values:")
for value in sach.values():
    print(value)

print("Tất cả cặp key-value:")
for key, value in sach.items():
    print(f"{key}: {value}")

# CÂU HỎI 4:
# a) Tạo hai sets
so_chan = {0, 2, 4, 6, 8, 10}
so_chia_het_cho_3 = {0, 3, 6, 9}
print(f"Set số chẵn: {so_chan}")
print(f"Set số chia hết cho 3: {so_chia_het_cho_3}")

# b) Tìm hợp
hop = so_chan.union(so_chia_het_cho_3)
print(f"Hợp của hai sets: {hop}")

# c) Tìm giao
giao = so_chan.intersection(so_chia_het_cho_3)
print(f"Giao của hai sets: {giao}")

# d) Tìm hiệu
hieu = so_chan.difference(so_chia_het_cho_3)
print(f"Hiệu của set chẵn trừ set chia hết cho 3: {hieu}")

# e) Kiểm tra tập con
set_moi = {0, 2, 4, 6, 8, 10, 12, 14}
if so_chan.issubset(set_moi):
    print("Set số chẵn là tập con của set mới")
else:
    print("Set số chẵn không phải là tập con của set mới")

# BÀI TẬP NÂNG CAO 1:
def quan_ly_sinh_vien():
    danh_sach_sv = []
    
    while True:
        print("\n===== QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên mới")
        print("2. Tìm kiếm sinh viên theo ID")
        print("3. Cập nhật thông tin sinh viên")
        print("4. Xóa sinh viên")
        print("5. Hiển thị danh sách sinh viên")
        print("0. Thoát")
        
        lua_chon = input("Nhập lựa chọn của bạn: ")
        
        if lua_chon == "1":
            # Thêm sinh viên mới
            id_sv = input("Nhập ID sinh viên: ")
            
            # Kiểm tra ID đã tồn tại chưa
            if any(sv["id"] == id_sv for sv in danh_sach_sv):
                print("ID sinh viên đã tồn tại!")
                continue
                
            ten = input("Nhập tên sinh viên: ")
            try:
                diem = float(input("Nhập điểm trung bình: "))
                if diem < 0 or diem > 10:
                    print("Điểm phải nằm trong khoảng 0-10!")
                    continue
            except ValueError:
                print("Điểm phải là số!")
                continue
                
            sinh_vien = {"id": id_sv, "ten": ten, "diem": diem}
            danh_sach_sv.append(sinh_vien)
            print("Thêm sinh viên thành công!")
            
        elif lua_chon == "2":
            # Tìm kiếm sinh viên
            id_sv = input("Nhập ID sinh viên cần tìm: ")
            
            found = False
            for sv in danh_sach_sv:
                if sv["id"] == id_sv:
                    print(f"Thông tin sinh viên:")
                    print(f"ID: {sv['id']}")
                    print(f"Tên: {sv['ten']}")
                    print(f"Điểm trung bình: {sv['diem']}")
                    found = True
                    break
                    
            if not found:
                print("Không tìm thấy sinh viên với ID này!")
                
        elif lua_chon == "3":
            # Cập nhật thông tin sinh viên
            id_sv = input("Nhập ID sinh viên cần cập nhật: ")
            
            found = False
            for sv in danh_sach_sv:
                if sv["id"] == id_sv:
                    ten_moi = input(f"Nhập tên mới (hiện tại: {sv['ten']}): ")
                    if ten_moi:  # Nếu người dùng nhập tên mới
                        sv["ten"] = ten_moi
                        
                    try:
                        diem_moi = input(f"Nhập điểm mới (hiện tại: {sv['diem']}): ")
                        if diem_moi:  # Nếu người dùng nhập điểm mới
                            diem_moi = float(diem_moi)
                            if diem_moi < 0 or diem_moi > 10:
                                print("Điểm phải nằm trong khoảng 0-10!")
                            else:
                                sv["diem"] = diem_moi
                    except ValueError:
                        print("Điểm phải là số!")
                    
                    print("Cập nhật thông tin thành công!")
                    found = True
                    break
                    
            if not found:
                print("Không tìm thấy sinh viên với ID này!")
                
        elif lua_chon == "4":
            # Xóa sinh viên
            id_sv = input("Nhập ID sinh viên cần xóa: ")
            
            found = False
            for i, sv in enumerate(danh_sach_sv):
                if sv["id"] == id_sv:
                    xac_nhan = input(f"Bạn có chắc muốn xóa sinh viên {sv['ten']} (y/n)? ")
                    if xac_nhan.lower() == 'y':
                        danh_sach_sv.pop(i)
                        print("Xóa sinh viên thành công!")
                    found = True
                    break
                    
            if not found:
                print("Không tìm thấy sinh viên với ID này!")
                
        elif lua_chon == "5":
            # Hiển thị danh sách sinh viên
            if not danh_sach_sv:
                print("Danh sách sinh viên trống!")
            else:
                # Sắp xếp theo điểm giảm dần
                danh_sach_sv_sorted = sorted(danh_sach_sv, key=lambda x: x["diem"], reverse=True)
                
                print("\nDANH SÁCH SINH VIÊN (theo điểm giảm dần):")
                print(f"{'ID':<10}{'Tên':<30}{'Điểm TB':<10}")
                print("-" * 50)
                
                for sv in danh_sach_sv_sorted:
                    print(f"{sv['id']:<10}{sv['ten']:<30}{sv['diem']:<10.2f}")
                    
        elif lua_chon == "0":
            print("Tạm biệt!")
            break
            
        else:
            print("Lựa chọn không hợp lệ!")

# Chạy chương trình quản lý sinh viên
# quan_ly_sinh_vien()

# BÀI TẬP NÂNG CAO 2:
import string

def dem_tan_suat_tu():
    # a) Đọc văn bản từ người dùng
    van_ban = input("Nhập văn bản: ")
    
    # b) Chuyển văn bản thành chữ thường và loại bỏ dấu câu
    van_ban = van_ban.lower()
    for char in string.punctuation:
        van_ban = van_ban.replace(char, " ")
    
    # c) Tách văn bản thành các từ
    cac_tu = van_ban.split()
    
    # d) Đếm số lần xuất hiện của mỗi từ
    tan_suat = {}
    for tu in cac_tu:
        if tu in tan_suat:
            tan_suat[tu] += 1
        else:
            tan_suat[tu] = 1
    
    # e) Hiển thị 5 từ xuất hiện nhiều nhất
    tu_pho_bien = sorted(tan_suat.items(), key=lambda x: x[1], reverse=True)
    
    print("\nTần suất xuất hiện của các từ:")
    for tu, so_lan in tan_suat.items():
        print(f"{tu}: {so_lan}")
    
    print("\n5 từ xuất hiện nhiều nhất:")
    for i, (tu, so_lan) in enumerate(tu_pho_bien[:5], 1):
        print(f"{i}. {tu}: {so_lan}")

# Chạy chương trình đếm tần suất từ
# dem_tan_suat_tu()

# BÀI TẬP NÂNG CAO 3:
import json
import os

def tu_dien_anh_viet():
    # Khởi tạo từ điển
    tu_dien = {}
    
    # Đọc từ điển từ file nếu tồn tại
    file_path = "tu_dien_anh_viet.json"
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                tu_dien = json.load(file)
            print(f"Đã đọc từ điển từ file với {len(tu_dien)} từ.")
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")
    
    while True:
        print("\n===== TỪ ĐIỂN ANH-VIỆT =====")
        print("1. Thêm từ mới")
        print("2. Tìm kiếm từ")
        print("3. Cập nhật nghĩa của từ")
        print("4. Xóa từ")
        print("5. Hiển thị toàn bộ từ điển")
        print("6. Lưu từ điển vào file")
        print("0. Thoát")
        
        lua_chon = input("Nhập lựa chọn của bạn: ")
        
        if lua_chon == "1":
            # Thêm từ mới
            tu_tieng_anh = input("Nhập từ tiếng Anh: ").strip().lower()
            
            if tu_tieng_anh in tu_dien:
                print(f"Từ '{tu_tieng_anh}' đã tồn tại trong từ điển!")
                continue
                
            nghia_tieng_viet = input("Nhập nghĩa tiếng Việt: ").strip()
            vi_du = input("Nhập ví dụ (nếu có): ").strip()
            
            tu_dien[tu_tieng_anh] = {
                "nghia": nghia_tieng_viet,
                "vi_du": vi_du
            }
            
            print(f"Đã thêm từ '{tu_tieng_anh}' vào từ điển!")
            
        elif lua_chon == "2":
            # Tìm kiếm từ
            tu_tieng_anh = input("Nhập từ cần tìm: ").strip().lower()
            
            if tu_tieng_anh in tu_dien:
                print(f"\nTừ: {tu_tieng_anh}")
                print(f"Nghĩa: {tu_dien[tu_tieng_anh]['nghia']}")
                if tu_dien[tu_tieng_anh]['vi_du']:
                    print(f"Ví dụ: {tu_dien[tu_tieng_anh]['vi_du']}")
            else:
                print(f"Không tìm thấy từ '{tu_tieng_anh}' trong từ điển!")
                
        elif lua_chon == "3":
            # Cập nhật nghĩa của từ
            tu_tieng_anh = input("Nhập từ cần cập nhật: ").strip().lower()
            
            if tu_tieng_anh in tu_dien:
                nghia_moi = input(f"Nhập nghĩa mới (hiện tại: {tu_dien[tu_tieng_anh]['nghia']}): ").strip()
                if nghia_moi:
                    tu_dien[tu_tieng_anh]['nghia'] = nghia_moi
                
                vi_du_moi = input(f"Nhập ví dụ mới (hiện tại: {tu_dien[tu_tieng_anh]['vi_du']}): ").strip()
                if vi_du_moi:
                    tu_dien[tu_tieng_anh]['vi_du'] = vi_du_moi
                
                print(f"Đã cập nhật từ '{tu_tieng_anh}'!")
            else:
                print(f"Không tìm thấy từ '{tu_tieng_anh}' trong từ điển!")
                
        elif lua_chon == "4":
            # Xóa từ
            tu_tieng_anh = input("Nhập từ cần xóa: ").strip().lower()
            
            if tu_tieng_anh in tu_dien:
                xac_nhan = input(f"Bạn có chắc muốn xóa từ '{tu_tieng_anh}' (y/n)? ")
                if xac_nhan.lower() == 'y':
                    del tu_dien[tu_tieng_anh]
                    print(f"Đã xóa từ '{tu_tieng_anh}' khỏi từ điển!")
            else:
                print(f"Không tìm thấy từ '{tu_tieng_anh}' trong từ điển!")
                
        elif lua_chon == "5":
            # Hiển thị toàn bộ từ điển
            if not tu_dien:
                print("Từ điển trống!")
            else:
                print("\nTỪ ĐIỂN ANH-VIỆT:")
                print("-" * 50)
                
                # Sắp xếp từ điển theo thứ tự bảng chữ cái
                for tu in sorted(tu_dien.keys()):
                    print(f"Từ: {tu}")
                    print(f"Nghĩa: {tu_dien[tu]['nghia']}")
                    if tu_dien[tu]['vi_du']:
                        print(f"Ví dụ: {tu_dien[tu]['vi_du']}")
                    print("-" * 50)
                    
        elif lua_chon == "6":
            # Lưu từ điển vào file
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(tu_dien, file, ensure_ascii=False, indent=4)
                print(f"Đã lưu từ điển vào file {file_path}!")
            except Exception as e:
                print(f"Lỗi khi lưu file: {e}")
                
        elif lua_chon == "0":
            # Hỏi người dùng có muốn lưu trước khi thoát không
            if tu_dien:
                luu = input("Bạn có muốn lưu từ điển trước khi thoát (y/n)? ")
                if luu.lower() == 'y':
                    try:
                        with open(file_path, "w", encoding="utf-8") as file:
                            json.dump(tu_dien, file, ensure_ascii=False, indent=4)
                        print(f"Đã lưu từ điển vào file {file_path}!")
                    except Exception as e:
                        print(f"Lỗi khi lưu file: {e}")
            
            print("Tạm biệt!")
            break
            
        else:
            print("Lựa chọn không hợp lệ!")

# Chạy chương trình từ điển Anh-Việt
# tu_dien_anh_viet()
"""

