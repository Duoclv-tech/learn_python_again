"""
PHẦN 9: OBJECT-ORIENTED PROGRAMMING TRONG PYTHON
=========================================

Bài tập từ cơ bản đến nâng cao để luyện tập về lập trình hướng đối tượng trong Python.
"""

# CÂU HỎI 1: Classes và objects
# a) Tạo một class Person với các thuộc tính name và age
# b) Tạo phương thức introduce() để in ra "Xin chào, tôi là {name} và tôi {age} tuổi."
# c) Tạo hai đối tượng từ class Person và gọi phương thức introduce() cho mỗi đối tượng

# Code của bạn ở đây:




# CÂU HỎI 2: Attributes và methods
# a) Tạo một class Rectangle với các thuộc tính width và height
# b) Tạo các phương thức calculate_area(), calculate_perimeter() và is_square()
# c) Tạo một đối tượng Rectangle và gọi các phương thức của nó

# Code của bạn ở đây:




# CÂU HỎI 3: Constructor (__init__)
# a) Tạo một class BankAccount với constructor nhận account_number, owner_name và initial_balance
# b) Tạo các phương thức deposit(amount), withdraw(amount) và get_balance()
# c) Tạo một đối tượng BankAccount và thực hiện các giao dịch

# Code của bạn ở đây:




# CÂU HỎI 4: Inheritance (Kế thừa)
# a) Tạo một class Animal với thuộc tính name và phương thức make_sound()
# b) Tạo các class Dog và Cat kế thừa từ Animal, ghi đè phương thức make_sound()
# c) Tạo các đối tượng từ các class Dog và Cat và gọi phương thức make_sound()

# Code của bạn ở đây:




# CÂU HỎI 5: Encapsulation (Đóng gói)
# a) Tạo một class Employee với thuộc tính private __salary
# b) Tạo các phương thức get_salary() và set_salary() để truy cập và thay đổi __salary
# c) Đảm bảo rằng salary không thể là số âm
# d) Tạo một đối tượng Employee và thử thay đổi salary

# Code của bạn ở đây:




# CÂU HỎI 6: Polymorphism (Đa hình)
# a) Tạo một class Shape với phương thức calculate_area()
# b) Tạo các class Circle và Square kế thừa từ Shape, ghi đè phương thức calculate_area()
# c) Tạo một hàm print_area(shape) nhận một đối tượng Shape và in ra diện tích của nó
# d) Gọi hàm print_area() với các đối tượng Circle và Square

# Code của bạn ở đây:




# BÀI TẬP NÂNG CAO 1:
# Xây dựng hệ thống quản lý thư viện với các class:
# - Book: title, author, isbn, available (boolean)
# - Library: books (list of Book objects)
# - Member: name, member_id, borrowed_books (list of Book objects)
#
# Các phương thức cần có:
# - Library.add_book(book): Thêm sách vào thư viện
# - Library.remove_book(isbn): Xóa sách khỏi thư viện
# - Library.search_book(title): Tìm sách theo tên
# - Member.borrow_book(library, isbn): Mượn sách từ thư viện
# - Member.return_book(library, isbn): Trả sách về thư viện
#
# Đảm bảo xử lý các trường hợp:
# - Không thể mượn sách đã được mượn
# - Không thể trả sách không thuộc về thư viện
# - Hiển thị thông báo phù hợp khi có lỗi

# Code của bạn ở đây:




# BÀI TẬP NÂNG CAO 2:
# Xây dựng hệ thống quản lý nhân viên với các class:
# - Person: name, age, address
# - Employee(Person): employee_id, position, department, salary
# - Manager(Employee): managed_employees (list of Employee objects)
# - Company: name, employees (list of Employee objects)
#
# Các phương thức cần có:
# - Company.hire_employee(employee): Thêm nhân viên vào công ty
# - Company.fire_employee(employee_id): Sa thải nhân viên
# - Company.give_raise(employee_id, amount): Tăng lương cho nhân viên
# - Manager.add_employee(employee): Thêm nhân viên vào danh sách quản lý
# - Manager.remove_employee(employee_id): Xóa nhân viên khỏi danh sách quản lý
# - Manager.display_team(): Hiển thị thông tin về team
#
# Đảm bảo xử lý các trường hợp đặc biệt và hiển thị thông báo phù hợp

# Code của bạn ở đây:




"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Xin chào, tôi là {self.name} và tôi {self.age} tuổi.")

# Tạo hai đối tượng Person
person1 = Person("Nguyễn Văn A", 25)
person2 = Person("Trần Thị B", 30)

# Gọi phương thức introduce()
person1.introduce()
person2.introduce()

# CÂU HỎI 2:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height

# Tạo một đối tượng Rectangle
rect = Rectangle(5, 3)
print(f"Diện tích: {rect.calculate_area()}")
print(f"Chu vi: {rect.calculate_perimeter()}")
print(f"Là hình vuông: {rect.is_square()}")

square = Rectangle(4, 4)
print(f"Diện tích: {square.calculate_area()}")
print(f"Chu vi: {square.calculate_perimeter()}")
print(f"Là hình vuông: {square.is_square()}")

# CÂU HỎI 3:
class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Đã nạp {amount} vào tài khoản. Số dư mới: {self.balance}")
        else:
            print("Số tiền nạp phải lớn hơn 0")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Đã rút {amount} từ tài khoản. Số dư mới: {self.balance}")
            else:
                print("Số dư không đủ")
        else:
            print("Số tiền rút phải lớn hơn 0")
    
    def get_balance(self):
        return self.balance

# Tạo một đối tượng BankAccount
account = BankAccount("12345", "Nguyễn Văn A", 1000)
print(f"Số dư ban đầu: {account.get_balance()}")

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Số dư không đủ
print(f"Số dư cuối cùng: {account.get_balance()}")

# CÂU HỎI 4:
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Động vật kêu")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} sủa: Gâu gâu!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} kêu: Meo meo!")

# Tạo các đối tượng
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Gọi phương thức make_sound()
dog.make_sound()
cat.make_sound()

# CÂU HỎI 5:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = 0  # Private attribute
        self.set_salary(salary)  # Sử dụng setter để kiểm tra giá trị
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Lương không thể là số âm")
    
    def display_info(self):
        print(f"Nhân viên: {self.name}, Lương: {self.__salary}")

# Tạo một đối tượng Employee
emp = Employee("Nguyễn Văn A", 5000)
emp.display_info()

# Thử thay đổi lương
emp.set_salary(6000)
emp.display_info()

emp.set_salary(-1000)  # Lương không thể là số âm
emp.display_info()

# Thử truy cập trực tiếp vào __salary (sẽ gây lỗi hoặc tạo thuộc tính mới)
# emp.__salary = -2000  # Không thay đổi thuộc tính private thực sự
# emp.display_info()

# CÂU HỎI 6:
import math

class Shape:
    def calculate_area(self):
        pass  # Abstract method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2

def print_area(shape):
    print(f"Diện tích của hình là: {shape.calculate_area():.2f}")

# Tạo các đối tượng
circle = Circle(5)
square = Square(4)

# Gọi hàm print_area() với các đối tượng khác nhau
print_area(circle)
print_area(square)

# BÀI TẬP NÂNG CAO 1:
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
    
    def __str__(self):
        status = "Có sẵn" if self.available else "Đã được mượn"
        return f"'{self.title}' bởi {self.author} (ISBN: {self.isbn}) - {status}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Đã thêm sách '{book.title}' vào thư viện {self.name}")
    
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Đã xóa sách có ISBN {isbn} khỏi thư viện")
                return True
        print(f"Không tìm thấy sách có ISBN {isbn} trong thư viện")
        return False
    
    def search_book(self, title):
        found_books = []
        for book in self.books:
            if title.lower() in book.title.lower():
                found_books.append(book)
        
        if found_books:
            print(f"Tìm thấy {len(found_books)} sách với tiêu đề '{title}':")
            for book in found_books:
                print(f"  - {book}")
            return found_books
        else:
            print(f"Không tìm thấy sách nào với tiêu đề '{title}'")
            return []
    
    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def display_all_books(self):
        if not self.books:
            print(f"Thư viện {self.name} không có sách nào")
            return
        
        print(f"Danh sách sách trong thư viện {self.name}:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, library, isbn):
        book = library.find_book_by_isbn(isbn)
        
        if not book:
            print(f"Không tìm thấy sách có ISBN {isbn} trong thư viện")
            return False
        
        if not book.available:
            print(f"Sách '{book.title}' hiện không có sẵn để mượn")
            return False
        
        book.available = False
        self.borrowed_books.append(book)
        print(f"{self.name} đã mượn sách '{book.title}'")
        return True
    
    def return_book(self, library, isbn):
        # Kiểm tra xem sách có trong danh sách đã mượn không
        for i, book in enumerate(self.borrowed_books):
            if book.isbn == isbn:
                # Kiểm tra xem sách có thuộc thư viện không
                lib_book = library.find_book_by_isbn(isbn)
                if lib_book:
                    lib_book.available = True
                    returned_book = self.borrowed_books.pop(i)
                    print(f"{self.name} đã trả sách '{returned_book.title}'")
                    return True
                else:
                    print(f"Sách này không thuộc về thư viện {library.name}")
                    return False
        
        print(f"Bạn không mượn sách có ISBN {isbn}")
        return False
    
    def display_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} chưa mượn sách nào")
            return
        
        print(f"Sách {self.name} đã mượn:")
        for i, book in enumerate(self.borrowed_books, 1):
            print(f"{i}. {book}")

# Kiểm tra hệ thống quản lý thư viện
def test_library_system():
    # Tạo thư viện
    library = Library("Thư viện Công cộng")
    
    # Tạo sách
    book1 = Book("Python Programming", "John Smith", "978-1-123456-78-9")
    book2 = Book("Data Science Basics", "Jane Doe", "978-2-987654-32-1")
    book3 = Book("Machine Learning", "Robert Johnson", "978-3-456789-01-2")
    
    # Thêm sách vào thư viện
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # Hiển thị tất cả sách
    library.display_all_books()
    
    # Tìm kiếm sách
    print("\nTìm kiếm sách:")
    library.search_book("Python")
    library.search_book("Java")  # Không tìm thấy
    
    # Tạo thành viên
    member1 = Member("Nguyễn Văn A", "M001")
    member2 = Member("Trần Thị B", "M002")
    
    # Mượn sách
    print("\nMượn sách:")
    member1.borrow_book(library, "978-1-123456-78-9")  # Python Programming
    member1.borrow_book(library, "978-3-456789-01-2")  # Machine Learning
    member2.borrow_book(library, "978-2-987654-32-1")  # Data Science Basics
    
    # Thử mượn sách đã được mượn
    member2.borrow_book(library, "978-1-123456-78-9")  # Đã được mượn
    
    # Hiển thị sách đã mượn
    print("\nSách đã mượn:")
    member1.display_borrowed_books()
    member2.display_borrowed_books()
    
    # Hiển thị tất cả sách trong thư viện (để xem trạng thái)
    print("\nSách trong thư viện sau khi mượn:")
    library.display_all_books()
    
    # Trả sách
    print("\nTrả sách:")
    member1.return_book(library, "978-1-123456-78-9")  # Trả Python Programming
    
    # Thử trả sách không mượn
    member1.return_book(library, "978-2-987654-32-1")  # Không mượn sách này
    
    # Hiển thị sách đã mượn sau khi trả
    print("\nSách đã mượn sau khi trả:")
    member1.display_borrowed_books()
    
    # Hiển thị tất cả sách trong thư viện sau khi trả
    print("\nSách trong thư viện sau khi trả:")
    library.display_all_books()

# Chạy kiểm tra
# test_library_system()

# BÀI TẬP NÂNG CAO 2:
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def display_info(self):
        return f"Tên: {self.name}, Tuổi: {self.age}, Địa chỉ: {self.address}"

class Employee(Person):
    def __init__(self, name, age, address, employee_id, position, department, salary):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.position = position
        self.department = department
        self.salary = salary
    
    def display_info(self):
        basic_info = super().display_info()
        return f"{basic_info}\nID: {self.employee_id}, Vị trí: {self.position}, Phòng ban: {self.department}, Lương: {self.salary}"
    
    def __str__(self):
        return f"Nhân viên {self.name} (ID: {self.employee_id}) - {self.position}"

class Manager(Employee):
    def __init__(self, name, age, address, employee_id, department, salary):
        super().__init__(name, age, address, employee_id, "Manager", department, salary)
        self.managed_employees = []
    
    def add_employee(self, employee):
        if employee.employee_id != self.employee_id:  # Không thể quản lý chính mình
            self.managed_employees.append(employee)
            print(f"Đã thêm {employee.name} vào team của {self.name}")
            return True
        else:
            print("Manager không thể quản lý chính mình")
            return False
    
    def remove_employee(self, employee_id):
        for i, emp in enumerate(self.managed_employees):
            if emp.employee_id == employee_id:
                removed_emp = self.managed_employees.pop(i)
                print(f"Đã xóa {removed_emp.name} khỏi team của {self.name}")
                return True
        
        print(f"Không tìm thấy nhân viên có ID {employee_id} trong team")
        return False
    
    def display_team(self):
        if not self.managed_employees:
            print(f"{self.name} chưa quản lý nhân viên nào")
            return
        
        print(f"Team của {self.name} ({len(self.managed_employees)} nhân viên):")
        for i, emp in enumerate(self.managed_employees, 1):
            print(f"{i}. {emp}")

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def hire_employee(self, employee):
        # Kiểm tra xem employee_id đã tồn tại chưa
        for emp in self.employees:
            if emp.employee_id == employee.employee_id:
                print(f"Nhân viên với ID {employee.employee_id} đã tồn tại trong công ty")
                return False
        
        self.employees.append(employee)
        print(f"Đã thuê {employee.name} vào công ty {self.name}")
        return True
    
    def fire_employee(self, employee_id):
        for i, emp in enumerate(self.employees):
            if emp.employee_id == employee_id:
                fired_emp = self.employees.pop(i)
                print(f"Đã sa thải {fired_emp.name} khỏi công ty {self.name}")
                
                # Nếu là manager, cần xóa nhân viên này khỏi danh sách quản lý của các manager khác
                for manager in self.get_all_managers():
                    manager.remove_employee(employee_id)
                
                return True
        
        print(f"Không tìm thấy nhân viên có ID {employee_id} trong công ty")
        return False
    
    def give_raise(self, employee_id, amount):
        if amount <= 0:
            print("Số tiền tăng lương phải lớn hơn 0")
            return False
        
        for emp in self.employees:
            if emp.employee_id == employee_id:
                emp.salary += amount
                print(f"Đã tăng lương {amount} cho {emp.name}. Lương mới: {emp.salary}")
                return True
        
        print(f"Không tìm thấy nhân viên có ID {employee_id} trong công ty")
        return False
    
    def get_all_managers(self):
        return [emp for emp in self.employees if isinstance(emp, Manager)]
    
    def find_employee_by_id(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        return None
    
    def display_all_employees(self):
        if not self.employees:
            print(f"Công ty {self.name} chưa có nhân viên nào")
            return
        
        print(f"Danh sách nhân viên của công ty {self.name} ({len(self.employees)} nhân viên):")
        for i, emp in enumerate(self.employees, 1):
            print(f"{i}. {emp}")
    
    def display_organization(self):
        managers = self.get_all_managers()
        
        if not managers:
            print(f"Công ty {self.name} chưa có manager nào")
            return
        
        print(f"Cơ cấu tổ chức của công ty {self.name}:")
        for manager in managers:
            print(f"\n--- Manager: {manager.name} ({manager.department}) ---")
            manager.display_team()

# Kiểm tra hệ thống quản lý nhân viên
def test_employee_management_system():
    # Tạo công ty
    company = Company("Tech Solutions")
    
    # Tạo các nhân viên và manager
    manager1 = Manager("Nguyễn Văn A", 35, "Hà Nội", "M001", "Engineering", 20000)
    manager2 = Manager("Trần Thị B", 40, "Hồ Chí Minh", "M002", "Marketing", 18000)
    
    emp1 = Employee("Lê Văn C", 25, "Hà Nội", "E001", "Developer", "Engineering", 10000)
    emp2 = Employee("Phạm Thị D", 28, "Đà Nẵng", "E002", "Developer", "Engineering", 12000)
    emp3 = Employee("Hoàng Văn E", 30, "Hồ Chí Minh", "E003", "Designer", "Marketing", 9000)
    
    # Thuê nhân viên và manager
    company.hire_employee(manager1)
    company.hire_employee(manager2)
    company.hire_employee(emp1)
    company.hire_employee(emp2)
    company.hire_employee(emp3)
    
    # Thêm nhân viên vào team của manager
    manager1.add_employee(emp1)
    manager1.add_employee(emp2)
    manager2.add_employee(emp3)
    
    # Hiển thị tất cả nhân viên
    print("\nDanh sách nhân viên:")
    company.display_all_employees()
    
    # Hiển thị cơ cấu tổ chức
    print("\nCơ cấu tổ chức:")
    company.display_organization()
    
    # Tăng lương cho nhân viên
    print("\nTăng lương:")
    company.give_raise("E001", 2000)
    company.give_raise("M002", 3000)
    
    # Sa thải nhân viên
    print("\nSa thải nhân viên:")
    company.fire_employee("E002")
    
    # Hiển thị cơ cấu tổ chức sau khi sa thải
    print("\nCơ cấu tổ chức sau khi sa thải:")
    company.display_organization()
    
    # Thêm nhân viên mới
    print("\nThêm nhân viên mới:")
    emp4 = Employee("Vũ Thị F", 27, "Hà Nội", "E004", "Tester", "Engineering", 11000)
    company.hire_employee(emp4)
    manager1.add_employee(emp4)
    
    # Hiển thị cơ cấu tổ chức cuối cùng
    print("\nCơ cấu tổ chức cuối cùng:")
    company.display_organization()

# Chạy kiểm tra
# test_employee_management_system()
"""
