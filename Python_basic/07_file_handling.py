"""
PHẦN 7: FILE HANDLING TRONG PYTHON
=========================================

Bài tập từ cơ bản đến nâng cao để luyện tập về xử lý file trong Python.
"""

# CÂU HỎI 1: Đọc và ghi file cơ bản
# a) Tạo một file văn bản có tên "hello.txt" và ghi vào đó dòng chữ "Xin chào Python!"
# b) Đọc nội dung của file "hello.txt" và in ra màn hình
# c) Ghi thêm dòng "Tôi đang học xử lý file" vào cuối file "hello.txt"
# d) Đọc và in ra từng dòng của file "hello.txt" kèm theo số dòng

# Code của bạn ở đây:




# CÂU HỎI 2: File modes và context managers
# a) Sử dụng context manager (with statement) để tạo file "numbers.txt" và ghi vào đó các số từ 1 đến 10, mỗi số trên một dòng
# b) Sử dụng context manager để đọc file "numbers.txt" và tính tổng các số trong file
# c) Giải thích sự khác biệt giữa các mode 'w', 'a', 'r', 'r+', 'w+', 'a+', 'b' khi mở file

# Code của bạn ở đây:




# CÂU HỎI 3: Working với CSV files
# a) Tạo một file CSV có tên "students.csv" với các cột: ID, Tên, Tuổi, Điểm trung bình
#    Thêm ít nhất 5 sinh viên vào file
# b) Đọc file "students.csv" và in ra thông tin của tất cả sinh viên
# c) Tìm sinh viên có điểm trung bình cao nhất
# d) Thêm một sinh viên mới vào file "students.csv"

# Code của bạn ở đây:




# CÂU HỎI 4: Working với JSON files
# a) Tạo một dictionary chứa thông tin về một cuốn sách (tiêu đề, tác giả, năm xuất bản, thể loại)
#    và lưu vào file "book.json"
# b) Đọc file "book.json" và in ra thông tin của cuốn sách
# c) Tạo một list chứa thông tin về 3 cuốn sách và lưu vào file "books.json"
# d) Đọc file "books.json" và in ra tên của tất cả các cuốn sách

# Code của bạn ở đây:




# CÂU HỎI 5: Path manipulation với pathlib
# a) Sử dụng pathlib để liệt kê tất cả các file .py trong thư mục hiện tại
# b) Tạo một thư mục mới có tên "data" nếu nó chưa tồn tại
# c) Di chuyển file "hello.txt" vào thư mục "data"
# d) Kiểm tra xem file "data/hello.txt" có tồn tại không và in ra kích thước của nó

# Code của bạn ở đây:




# BÀI TẬP NÂNG CAO 1:
# Viết chương trình quản lý danh sách công việc (to-do list) sử dụng file để lưu trữ
# Chương trình có các chức năng:
# - Thêm công việc mới
# - Xem danh sách công việc
# - Đánh dấu công việc đã hoàn thành
# - Xóa công việc
# - Lưu danh sách vào file JSON và đọc từ file khi khởi động

# Code của bạn ở đây:




# BÀI TẬP NÂNG CAO 2:
# Viết chương trình phân tích log file
# Cho một file log có định dạng: "YYYY-MM-DD HH:MM:SS [LEVEL] Message"
# Ví dụ: "2023-01-15 14:23:45 [ERROR] Connection failed"
# Chương trình cần:
# a) Đọc file log và phân loại các log theo level (INFO, WARNING, ERROR, etc.)
# b) Đếm số lượng log của mỗi level
# c) Tìm tất cả các ERROR log và lưu vào một file riêng
# d) Tạo báo cáo thống kê theo ngày (số lượng mỗi loại log cho mỗi ngày)

# Code của bạn ở đây:




"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
# a) Tạo một file văn bản có tên "hello.txt" và ghi vào đó dòng chữ "Xin chào Python!"
with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Xin chào Python!")

# b) Đọc nội dung của file "hello.txt" và in ra màn hình
with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# c) Ghi thêm dòng "Tôi đang học xử lý file" vào cuối file "hello.txt"
with open("hello.txt", "a", encoding="utf-8") as file:
    file.write("\nTôi đang học xử lý file")

# d) Đọc và in ra từng dòng của file "hello.txt" kèm theo số dòng
with open("hello.txt", "r", encoding="utf-8") as file:
    for i, line in enumerate(file, 1):
        print(f"Dòng {i}: {line.strip()}")

# CÂU HỎI 2:
# a) Sử dụng context manager (with statement) để tạo file "numbers.txt" và ghi vào đó các số từ 1 đến 10, mỗi số trên một dòng
with open("numbers.txt", "w", encoding="utf-8") as file:
    for i in range(1, 11):
        file.write(f"{i}\n")

# b) Sử dụng context manager để đọc file "numbers.txt" và tính tổng các số trong file
total = 0
with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        total += int(line.strip())
print(f"Tổng các số trong file: {total}")

# c) Giải thích sự khác biệt giữa các mode 'w', 'a', 'r', 'r+', 'w+', 'a+', 'b' khi mở file
'w': Mở file để ghi, tạo file mới nếu không tồn tại, xóa nội dung cũ nếu file đã tồn tại
'a': Mở file để ghi thêm vào cuối, tạo file mới nếu không tồn tại
'r': Mở file để đọc (mặc định), báo lỗi nếu file không tồn tại
'r+': Mở file để đọc và ghi, báo lỗi nếu file không tồn tại
'w+': Mở file để đọc và ghi, tạo file mới nếu không tồn tại, xóa nội dung cũ nếu file đã tồn tại
'a+': Mở file để đọc và ghi thêm vào cuối, tạo file mới nếu không tồn tại
'b': Thêm vào các mode trên để mở file ở chế độ nhị phân (binary)

# CÂU HỎI 3:
import csv

# a) Tạo một file CSV có tên "students.csv" với các cột: ID, Tên, Tuổi, Điểm trung bình
#    Thêm ít nhất 5 sinh viên vào file
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Tên", "Tuổi", "Điểm trung bình"])
    writer.writerow(["SV001", "Nguyễn Văn A", 20, 8.5])
    writer.writerow(["SV002", "Trần Thị B", 21, 9.0])
    writer.writerow(["SV003", "Lê Văn C", 19, 7.5])
    writer.writerow(["SV004", "Phạm Thị D", 22, 8.0])
    writer.writerow(["SV005", "Hoàng Văn E", 20, 8.8])

# b) Đọc file "students.csv" và in ra thông tin của tất cả sinh viên
with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)  # Bỏ qua header
    print("Danh sách sinh viên:")
    for row in reader:
        print(f"ID: {row[0]}, Tên: {row[1]}, Tuổi: {row[2]}, Điểm TB: {row[3]}")

# c) Tìm sinh viên có điểm trung bình cao nhất
with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)  # Bỏ qua header
    max_score = 0
    best_student = None
    for row in reader:
        score = float(row[3])
        if score > max_score:
            max_score = score
            best_student = row
    print(f"Sinh viên có điểm cao nhất: {best_student[1]} với điểm {best_student[3]}")

# d) Thêm một sinh viên mới vào file "students.csv"
with open("students.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["SV006", "Vũ Thị F", 21, 9.2])

# CÂU HỎI 4:
import json

# a) Tạo một dictionary chứa thông tin về một cuốn sách và lưu vào file "book.json"
book = {
    "title": "Python Programming",
    "author": "John Smith",
    "year": 2022,
    "genre": "Programming"
}

with open("book.json", "w", encoding="utf-8") as file:
    json.dump(book, file, indent=4)

# b) Đọc file "book.json" và in ra thông tin của cuốn sách
with open("book.json", "r", encoding="utf-8") as file:
    book_data = json.load(file)
    print("Thông tin sách:")
    for key, value in book_data.items():
        print(f"{key}: {value}")

# c) Tạo một list chứa thông tin về 3 cuốn sách và lưu vào file "books.json"
books = [
    {
        "title": "Python Programming",
        "author": "John Smith",
        "year": 2022,
        "genre": "Programming"
    },
    {
        "title": "Data Science with Python",
        "author": "Jane Doe",
        "year": 2021,
        "genre": "Data Science"
    },
    {
        "title": "Machine Learning Basics",
        "author": "Robert Johnson",
        "year": 2020,
        "genre": "Machine Learning"
    }
]

with open("books.json", "w", encoding="utf-8") as file:
    json.dump(books, file, indent=4)

# d) Đọc file "books.json" và in ra tên của tất cả các cuốn sách
with open("books.json", "r", encoding="utf-8") as file:
    books_data = json.load(file)
    print("Danh sách các cuốn sách:")
    for book in books_data:
        print(book["title"])

# CÂU HỎI 5:
from pathlib import Path

# a) Sử dụng pathlib để liệt kê tất cả các file .py trong thư mục hiện tại
current_dir = Path(".")
py_files = list(current_dir.glob("*.py"))
print("Các file .py trong thư mục hiện tại:")
for file in py_files:
    print(file.name)

# b) Tạo một thư mục mới có tên "data" nếu nó chưa tồn tại
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
print(f"Thư mục {data_dir} đã được tạo hoặc đã tồn tại.")

# c) Di chuyển file "hello.txt" vào thư mục "data"
hello_file = Path("hello.txt")
if hello_file.exists():
    target_file = data_dir / hello_file.name
    hello_file.rename(target_file)
    print(f"Đã di chuyển {hello_file} đến {target_file}")
else:
    print(f"File {hello_file} không tồn tại.")

# d) Kiểm tra xem file "data/hello.txt" có tồn tại không và in ra kích thước của nó
target_file = data_dir / "hello.txt"
if target_file.exists():
    print(f"File {target_file} tồn tại và có kích thước {target_file.stat().st_size} bytes.")
else:
    print(f"File {target_file} không tồn tại.")

# BÀI TẬP NÂNG CAO 1:
import json
from pathlib import Path

class ToDoList:
    def __init__(self, file_path="todo.json"):
        self.file_path = Path(file_path)
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        if self.file_path.exists():
            with open(self.file_path, "r", encoding="utf-8") as file:
                try:
                    self.tasks = json.load(file)
                except json.JSONDecodeError:
                    self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4)
    
    def add_task(self, task):
        task_id = len(self.tasks) + 1
        new_task = {
            "id": task_id,
            "task": task,
            "completed": False
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Đã thêm công việc: {task}")
    
    def view_tasks(self):
        if not self.tasks:
            print("Danh sách công việc trống.")
            return
        
        print("Danh sách công việc:")
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            print(f"{task['id']}. [{status}] {task['task']}")
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"Đã đánh dấu hoàn thành công việc: {task['task']}")
                return
        print(f"Không tìm thấy công việc có ID: {task_id}")
    
    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted_task = self.tasks.pop(i)
                self.save_tasks()
                print(f"Đã xóa công việc: {deleted_task['task']}")
                return
        print(f"Không tìm thấy công việc có ID: {task_id}")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\n=== QUẢN LÝ CÔNG VIỆC ===")
        print("1. Thêm công việc mới")
        print("2. Xem danh sách công việc")
        print("3. Đánh dấu công việc đã hoàn thành")
        print("4. Xóa công việc")
        print("0. Thoát")
        
        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == "1":
            task = input("Nhập công việc mới: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_id = int(input("Nhập ID công việc đã hoàn thành: "))
            todo_list.complete_task(task_id)
        elif choice == "4":
            task_id = int(input("Nhập ID công việc cần xóa: "))
            todo_list.delete_task(task_id)
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

# Để chạy chương trình, bỏ comment dòng dưới
# main()

# BÀI TẬP NÂNG CAO 2:
import re
from datetime import datetime
from collections import defaultdict
from pathlib import Path

def analyze_log_file(log_file_path):
    # Regex pattern để phân tích dòng log
    pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)"
    
    # Khởi tạo các biến để lưu kết quả phân tích
    logs_by_level = defaultdict(list)
    logs_by_date = defaultdict(lambda: defaultdict(int))
    
    # Đọc file log
    with open(log_file_path, "r", encoding="utf-8") as file:
        for line in file:
            match = re.match(pattern, line.strip())
            if match:
                date, time, level, message = match.groups()
                
                # Lưu log theo level
                logs_by_level[level].append((date, time, message))
                
                # Đếm log theo ngày và level
                logs_by_date[date][level] += 1
    
    # a) Phân loại các log theo level
    print("=== PHÂN LOẠI LOG THEO LEVEL ===")
    for level, logs in logs_by_level.items():
        print(f"{level}: {len(logs)} logs")
    
    # b) Đếm số lượng log của mỗi level
    print("\n=== SỐ LƯỢNG LOG THEO LEVEL ===")
    for level, logs in logs_by_level.items():
        print(f"{level}: {len(logs)}")
    
    # c) Lưu các ERROR log vào file riêng
    if "ERROR" in logs_by_level:
        error_log_path = Path(log_file_path).parent / "error_logs.txt"
        with open(error_log_path, "w", encoding="utf-8") as error_file:
            for date, time, message in logs_by_level["ERROR"]:
                error_file.write(f"{date} {time} [ERROR] {message}\n")
        print(f"\nĐã lưu {len(logs_by_level['ERROR'])} ERROR logs vào file {error_log_path}")
    
    # d) Tạo báo cáo thống kê theo ngày
    print("\n=== BÁO CÁO THỐNG KÊ THEO NGÀY ===")
    for date, levels in sorted(logs_by_date.items()):
        print(f"Ngày {date}:")
        for level, count in levels.items():
            print(f"  - {level}: {count} logs")

# Để chạy chương trình, tạo một file log mẫu và bỏ comment dòng dưới
# analyze_log_file("sample_log.txt")
"""
