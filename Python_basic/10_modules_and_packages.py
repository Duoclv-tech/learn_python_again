"""
PHẦN 10: MODULES VÀ PACKAGES TRONG PYTHON
=========================================

Bài tập từ cơ bản đến nâng cao để luyện tập về modules và packages trong Python.
"""

# CÂU HỎI 1: Importing modules
# a) Import module math và sử dụng các hàm sin, cos, sqrt
# b) Import module random và tạo một số ngẫu nhiên từ 1 đến 100
# c) Import module datetime và hiển thị ngày giờ hiện tại
# d) Import module sys và in ra đường dẫn tìm kiếm module (sys.path)

# Code của bạn ở đây:




# CÂU HỎI 2: Creating modules
# a) Tạo một file my_math.py với các hàm add, subtract, multiply, divide
# b) Import các hàm từ my_math và sử dụng chúng
# c) Import toàn bộ module my_math và sử dụng các hàm thông qua namespace
# d) Import module my_math với alias

# Code của bạn ở đây:




# CÂU HỎI 3: Package structure
# a) Tạo một package có tên my_package với cấu trúc:
#    my_package/
#    ├── __init__.py
#    ├── module1.py
#    └── module2.py
# b) Trong module1.py, định nghĩa hàm hello()
# c) Trong module2.py, định nghĩa hàm goodbye()
# d) Import và sử dụng các hàm từ package

# Code của bạn ở đây:




# CÂU HỎI 4: __init__.py files
# a) Trong file __init__.py của my_package, import các hàm hello và goodbye
# b) Sử dụng các hàm trực tiếp từ my_package mà không cần import từ các module con

# Code của bạn ở đây:




# CÂU HỎI 5: Virtual environments
# a) Giải thích mục đích của virtual environment trong Python
# b) Liệt kê các bước để tạo và kích hoạt virtual environment
# c) Giải thích cách cài đặt packages trong virtual environment
# d) Giải thích cách export và import danh sách packages (requirements.txt)

# Câu trả lời của bạn ở đây:




# BÀI TẬP NÂNG CAO 1:
# Xây dựng một package quản lý sinh viên với cấu trúc:
# student_manager/
# ├── __init__.py
# ├── models/
# │   ├── __init__.py
# │   └── student.py (định nghĩa class Student)
# ├── utils/
# │   ├── __init__.py
# │   └── file_handler.py (các hàm để đọc/ghi file CSV)
# └── services/
#     ├── __init__.py
#     └── student_service.py (các hàm để thêm, xóa, sửa, tìm kiếm sinh viên)
#
# Viết code để tạo package này và sử dụng nó để quản lý danh sách sinh viên

# Code của bạn ở đây:




# BÀI TẬP NÂNG CAO 2:
# Tạo một CLI (Command Line Interface) application sử dụng argparse module
# Application này cho phép:
# - Thêm sinh viên: python app.py add --name "Nguyen Van A" --age 20 --score 8.5
# - Hiển thị danh sách sinh viên: python app.py list
# - Tìm kiếm sinh viên: python app.py search --name "Nguyen"
# - Xóa sinh viên: python app.py delete --id 1
#
# Sử dụng package student_manager đã tạo ở bài tập trước

# Code của bạn ở đây:




'''
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
# a) Import module math và sử dụng các hàm sin, cos, sqrt
import math

angle = math.pi / 4  # 45 degrees
print(f"sin(45°) = {math.sin(angle)}")
print(f"cos(45°) = {math.cos(angle)}")
print(f"sqrt(16) = {math.sqrt(16)}")

# b) Import module random và tạo một số ngẫu nhiên từ 1 đến 100
import random

random_number = random.randint(1, 100)
print(f"Số ngẫu nhiên từ 1 đến 100: {random_number}")

# c) Import module datetime và hiển thị ngày giờ hiện tại
import datetime

now = datetime.datetime.now()
print(f"Ngày giờ hiện tại: {now}")
print(f"Ngày hiện tại: {now.strftime('%Y-%m-%d')}")
print(f"Giờ hiện tại: {now.strftime('%H:%M:%S')}")

# d) Import module sys và in ra đường dẫn tìm kiếm module (sys.path)
import sys

print("Đường dẫn tìm kiếm module:")
for path in sys.path:
    print(f"  - {path}")

# CÂU HỎI 2:
# a) Tạo một file my_math.py với các hàm add, subtract, multiply, divide

# Nội dung file my_math.py (tham khảo, không thực thi trực tiếp trong file này):
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Không thể chia cho 0")
    return a / b
"""

# b) Import các hàm từ my_math và sử dụng chúng
from my_math import add, subtract, multiply, divide

print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")
print(f"10 * 5 = {multiply(10, 5)}")
print(f"10 / 5 = {divide(10, 5)}")

# c) Import toàn bộ module my_math và sử dụng các hàm thông qua namespace
import my_math

print(f"10 + 5 = {my_math.add(10, 5)}")
print(f"10 - 5 = {my_math.subtract(10, 5)}")

# d) Import module my_math với alias
import my_math as mm

print(f"10 * 5 = {mm.multiply(10, 5)}")
print(f"10 / 5 = {mm.divide(10, 5)}")

# CÂU HỎI 3:
# a) Tạo một package có tên my_package với cấu trúc:
#    my_package/
#    ├── __init__.py
#    ├── module1.py
#    └── module2.py

# Nội dung file my_package/__init__.py (tham khảo):
"""
# Đây là file khởi tạo package
print("Khởi tạo my_package")
"""

# Nội dung file my_package/module1.py (tham khảo):
"""
def hello(name="World"):
    return f"Hello, {name}!"
"""

# Nội dung file my_package/module2.py (tham khảo):
"""
def goodbye(name="World"):
    return f"Goodbye, {name}!"
"""

# b) và c) và d) Import và sử dụng các hàm từ package
from my_package.module1 import hello
from my_package.module2 import goodbye

print(hello("Python"))
print(goodbye("Python"))

# Hoặc
import my_package.module1 as m1
import my_package.module2 as m2

print(m1.hello("User"))
print(m2.goodbye("User"))

# CÂU HỎI 4:
# a) Trong file __init__.py của my_package, import các hàm hello và goodbye

# Nội dung file my_package/__init__.py (tham khảo):
"""
# Import các hàm từ các module con
from .module1 import hello
from .module2 import goodbye

print("Khởi tạo my_package với hello và goodbye")
"""

# b) Sử dụng các hàm trực tiếp từ my_package mà không cần import từ các module con
import my_package

print(my_package.hello("Direct Import"))
print(my_package.goodbye("Direct Import"))

# CÂU HỎI 5:
# a) Giải thích mục đích của virtual environment trong Python
"""
Mục đích của virtual environment trong Python:
1. Tạo môi trường độc lập cho mỗi dự án, tránh xung đột về phiên bản package
2. Giúp quản lý dependencies riêng biệt cho từng dự án
3. Dễ dàng chia sẻ và tái tạo môi trường phát triển trên các máy khác
4. Tránh làm "ô nhiễm" môi trường Python hệ thống với quá nhiều packages
5. Cho phép sử dụng các phiên bản Python khác nhau cho các dự án khác nhau
"""

# b) Liệt kê các bước để tạo và kích hoạt virtual environment
"""
Các bước để tạo và kích hoạt virtual environment:

Với venv (có sẵn trong Python 3):
1. Tạo virtual environment:
   python -m venv myenv
   
2. Kích hoạt virtual environment:
   - Trên Windows:
     myenv\\Scripts\\activate
   - Trên macOS/Linux:
     source myenv/bin/activate
     
3. Để tắt virtual environment:
   deactivate

Với virtualenv (cần cài đặt riêng):
1. Cài đặt virtualenv:
   pip install virtualenv
   
2. Tạo virtual environment:
   virtualenv myenv
   
3. Kích hoạt và tắt giống như với venv
"""

# c) Giải thích cách cài đặt packages trong virtual environment
"""
Cách cài đặt packages trong virtual environment:

1. Đảm bảo virtual environment đã được kích hoạt (thấy tên môi trường ở đầu dòng lệnh)
2. Sử dụng pip để cài đặt packages:
   pip install package_name
   
3. Để cài đặt phiên bản cụ thể:
   pip install package_name==1.2.3
   
4. Để cài đặt nhiều packages cùng lúc:
   pip install package1 package2 package3
   
5. Để xem danh sách packages đã cài đặt:
   pip list
"""

# d) Giải thích cách export và import danh sách packages (requirements.txt)
"""
Cách export và import danh sách packages:

1. Export danh sách packages đã cài đặt:
   pip freeze > requirements.txt
   
2. Import (cài đặt) packages từ file requirements.txt:
   pip install -r requirements.txt
   
3. File requirements.txt có định dạng:
   package1==1.2.3
   package2>=2.0.0
   package3
   
4. Có thể thêm các ràng buộc phiên bản:
   == : phiên bản chính xác
   >= : phiên bản lớn hơn hoặc bằng
   <= : phiên bản nhỏ hơn hoặc bằng
   ~= : phiên bản tương thích (minor updates)
"""

# BÀI TẬP NÂNG CAO 1:
# Xây dựng một package quản lý sinh viên

# Tạo cấu trúc thư mục
"""
import os

def create_directory_structure():
    # Tạo cấu trúc thư mục
    os.makedirs("student_manager/models", exist_ok=True)
    os.makedirs("student_manager/utils", exist_ok=True)
    os.makedirs("student_manager/services", exist_ok=True)
    
    # Tạo các file __init__.py
    open("student_manager/__init__.py", "w").close()
    open("student_manager/models/__init__.py", "w").close()
    open("student_manager/utils/__init__.py", "w").close()
    open("student_manager/services/__init__.py", "w").close()
    
    print("Đã tạo cấu trúc thư mục package student_manager")

create_directory_structure()
"""

# Nội dung file student_manager/models/student.py
"""
class Student:
    def __init__(self, id, name, age, score):
        self.id = id
        self.name = name
        self.age = age
        self.score = score
    
    def __str__(self):
        return f"ID: {self.id}, Tên: {self.name}, Tuổi: {self.age}, Điểm: {self.score}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "score": self.score
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            name=data["name"],
            age=data["age"],
            score=data["score"]
        )
"""

# Nội dung file student_manager/utils/file_handler.py
"""
import csv
import os
from ..models.student import Student

def read_students_from_csv(file_path):
    students = []
    
    if not os.path.exists(file_path):
        return students
    
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Chuyển đổi kiểu dữ liệu
            row['id'] = int(row['id'])
            row['age'] = int(row['age'])
            row['score'] = float(row['score'])
            
            student = Student.from_dict(row)
            students.append(student)
    
    return students

def write_students_to_csv(students, file_path):
    if not students:
        return
    
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'name', 'age', 'score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for student in students:
            writer.writerow(student.to_dict())
"""

# Nội dung file student_manager/services/student_service.py
"""
from ..models.student import Student
from ..utils.file_handler import read_students_from_csv, write_students_to_csv

class StudentService:
    def __init__(self, file_path="students.csv"):
        self.file_path = file_path
        self.students = read_students_from_csv(file_path)
    
    def add_student(self, name, age, score):
        # Tạo ID mới
        new_id = 1
        if self.students:
            new_id = max(student.id for student in self.students) + 1
        
        # Tạo sinh viên mới
        student = Student(new_id, name, age, score)
        self.students.append(student)
        
        # Lưu vào file
        write_students_to_csv(self.students, self.file_path)
        
        return student
    
    def get_all_students(self):
        return self.students
    
    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None
    
    def search_students_by_name(self, name):
        return [student for student in self.students 
                if name.lower() in student.name.lower()]
    
    def update_student(self, student_id, name=None, age=None, score=None):
        student = self.get_student_by_id(student_id)
        if not student:
            return False
        
        if name is not None:
            student.name = name
        if age is not None:
            student.age = age
        if score is not None:
            student.score = score
        
        write_students_to_csv(self.students, self.file_path)
        return True
    
    def delete_student(self, student_id):
        student = self.get_student_by_id(student_id)
        if not student:
            return False
        
        self.students.remove(student)
        write_students_to_csv(self.students, self.file_path)
        return True
"""

# Nội dung file student_manager/__init__.py
"""
from .services.student_service import StudentService
"""

# Sử dụng package student_manager
"""
from student_manager import StudentService

def main():
    # Tạo service
    service = StudentService()
    
    # Thêm sinh viên
    service.add_student("Nguyễn Văn A", 20, 8.5)
    service.add_student("Trần Thị B", 21, 9.0)
    service.add_student("Lê Văn C", 19, 7.5)
    
    # Hiển thị danh sách sinh viên
    print("Danh sách sinh viên:")
    for student in service.get_all_students():
        print(student)
    
    # Tìm kiếm sinh viên
    print("\nTìm kiếm sinh viên có tên 'Nguyễn':")
    for student in service.search_students_by_name("Nguyễn"):
        print(student)
    
    # Cập nhật sinh viên
    print("\nCập nhật điểm cho sinh viên có ID = 1:")
    service.update_student(1, score=9.5)
    print(service.get_student_by_id(1))
    
    # Xóa sinh viên
    print("\nXóa sinh viên có ID = 2:")
    service.delete_student(2)
    
    # Hiển thị danh sách sau khi xóa
    print("\nDanh sách sinh viên sau khi xóa:")
    for student in service.get_all_students():
        print(student)

if __name__ == "__main__":
    main()
'''

# BÀI TẬP NÂNG CAO 2:
# Tạo một CLI application sử dụng argparse module

# Nội dung file app.py
"""
import argparse
from student_manager import StudentService

def setup_parser():
    parser = argparse.ArgumentParser(description='Quản lý sinh viên')
    subparsers = parser.add_subparsers(dest='command', help='Lệnh')
    
    # Lệnh add
    add_parser = subparsers.add_parser('add', help='Thêm sinh viên mới')
    add_parser.add_argument('--name', required=True, help='Tên sinh viên')
    add_parser.add_argument('--age', required=True, type=int, help='Tuổi sinh viên')
    add_parser.add_argument('--score', required=True, type=float, help='Điểm trung bình')
    
    # Lệnh list
    subparsers.add_parser('list', help='Hiển thị danh sách sinh viên')
    
    # Lệnh search
    search_parser = subparsers.add_parser('search', help='Tìm kiếm sinh viên')
    search_parser.add_argument('--name', required=True, help='Tên sinh viên cần tìm')
    
    # Lệnh update
    update_parser = subparsers.add_parser('update', help='Cập nhật thông tin sinh viên')
    update_parser.add_argument('--id', required=True, type=int, help='ID sinh viên')
    update_parser.add_argument('--name', help='Tên mới')
    update_parser.add_argument('--age', type=int, help='Tuổi mới')
    update_parser.add_argument('--score', type=float, help='Điểm mới')
    
    # Lệnh delete
    delete_parser = subparsers.add_parser('delete', help='Xóa sinh viên')
    delete_parser.add_argument('--id', required=True, type=int, help='ID sinh viên cần xóa')
    
    return parser

def main():
    parser = setup_parser()
    args = parser.parse_args()
    
    service = StudentService()
    
    if args.command == 'add':
        student = service.add_student(args.name, args.age, args.score)
        print(f"Đã thêm sinh viên: {student}")
    
    elif args.command == 'list':
        students = service.get_all_students()
        if not students:
            print("Danh sách sinh viên trống")
        else:
            print("Danh sách sinh viên:")
            for student in students:
                print(student)
    
    elif args.command == 'search':
        students = service.search_students_by_name(args.name)
        if not students:
            print(f"Không tìm thấy sinh viên nào có tên '{args.name}'")
        else:
            print(f"Kết quả tìm kiếm cho '{args.name}':")
            for student in students:
                print(student)
    
    elif args.command == 'update':
        success = service.update_student(args.id, args.name, args.age, args.score)
        if success:
            print(f"Đã cập nhật thông tin sinh viên có ID = {args.id}")
            print(service.get_student_by_id(args.id))
        else:
            print(f"Không tìm thấy sinh viên có ID = {args.id}")
    
    elif args.command == 'delete':
        success = service.delete_student(args.id)
        if success:
            print(f"Đã xóa sinh viên có ID = {args.id}")
        else:
            print(f"Không tìm thấy sinh viên có ID = {args.id}")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
"""
