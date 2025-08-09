"""
PHẦN 8: ERROR HANDLING TRONG PYTHON
=========================================

Bài tập từ cơ bản đến nâng cao để luyện tập về xử lý lỗi trong Python.
"""

# CÂU HỎI 1: Try, except cơ bản
# a) Viết một đoạn code để chia hai số, sử dụng try/except để xử lý trường hợp chia cho 0
# b) Sửa đoạn code sau để xử lý lỗi khi người dùng nhập không phải là số:
#    n = int(input("Nhập một số: "))
#    print(f"Bình phương của {n} là {n**2}")
# c) Viết code để mở và đọc một file, sử dụng try/except để xử lý trường hợp file không tồn tại

# Code của bạn ở đây:




# CÂU HỎI 2: Nhiều khối except
# a) Viết một đoạn code để chuyển đổi một chuỗi thành số và thực hiện phép chia
#    Xử lý riêng các lỗi: ValueError, ZeroDivisionError, và các lỗi khác
# b) Sửa đoạn code sau để xử lý các loại lỗi khác nhau:
#    filename = input("Nhập tên file: ")
#    with open(filename, 'r') as file:
#        content = file.read()
#        number = int(content)
#        result = 100 / number
#        print(f"Kết quả: {result}")

# Code của bạn ở đây:




# CÂU HỎI 3: Try, except, else, finally
# a) Viết code để nhập một số từ người dùng, sử dụng đầy đủ try, except, else, finally
#    - Trong khối try: Chuyển đổi input thành số nguyên
#    - Trong khối except: Xử lý lỗi nếu input không phải số
#    - Trong khối else: Tính bình phương của số đó
#    - Trong khối finally: In ra "Kết thúc xử lý input"
# b) Viết code để mở, đọc và xử lý một file, sử dụng đầy đủ try, except, else, finally

# Code của bạn ở đây:




# CÂU HỎI 4: Raising custom exceptions
# a) Tạo một custom exception có tên InvalidAgeError
# b) Viết một hàm validate_age(age) để kiểm tra tuổi:
#    - Nếu age không phải số: raise TypeError
#    - Nếu age < 0 hoặc age > 120: raise InvalidAgeError
#    - Nếu 0 <= age < 18: in "Bạn chưa đủ tuổi trưởng thành"
#    - Nếu 18 <= age <= 120: in "Bạn đã đủ tuổi trưởng thành"
# c) Gọi hàm validate_age với các giá trị khác nhau và xử lý các exceptions

# Code của bạn ở đây:




# CÂU HỎI 5: Logging
# a) Cấu hình logging để ghi log vào file "app.log" với format: thời gian, level, message
# b) Viết một hàm divide(a, b) để chia a cho b:
#    - Nếu b = 0: log lỗi với level ERROR và raise ZeroDivisionError
#    - Nếu a và b không phải số: log lỗi với level ERROR và raise TypeError
#    - Nếu phép chia thành công: log kết quả với level INFO
# c) Gọi hàm divide với các giá trị khác nhau

# Code của bạn ở đây:




# BÀI TẬP NÂNG CAO 1:
# Viết một class DatabaseConnection để mô phỏng kết nối đến cơ sở dữ liệu:
# - Phương thức connect(): mô phỏng kết nối đến DB, có thể raise ConnectionError
# - Phương thức execute_query(query): mô phỏng thực thi truy vấn, có thể raise SyntaxError hoặc ValueError
# - Phương thức close(): đóng kết nối
# 
# Sử dụng try/except/finally để đảm bảo kết nối luôn được đóng ngay cả khi có lỗi xảy ra
# Sử dụng logging để ghi lại các sự kiện và lỗi

# Code của bạn ở đây:




# BÀI TẬP NÂNG CAO 2:
# Viết một chương trình quản lý tài khoản ngân hàng với xử lý lỗi:
# - Class BankAccount có các thuộc tính: account_number, owner_name, balance
# - Class InsufficientFundsError kế thừa từ Exception
# - Class InvalidAmountError kế thừa từ Exception
# - Phương thức deposit(amount): thêm tiền vào tài khoản, raise InvalidAmountError nếu amount <= 0
# - Phương thức withdraw(amount): rút tiền, raise InvalidAmountError nếu amount <= 0,
#   raise InsufficientFundsError nếu amount > balance
# - Phương thức transfer(target_account, amount): chuyển tiền sang tài khoản khác
#
# Viết code để tạo các tài khoản và thực hiện các giao dịch với xử lý lỗi đầy đủ

# Code của bạn ở đây:




''' 
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
# a) Viết một đoạn code để chia hai số, sử dụng try/except để xử lý trường hợp chia cho 0
def divide_safely(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
        return None

# Kiểm tra hàm
print(divide_safely(10, 2))  # 5.0
print(divide_safely(10, 0))  # Lỗi: Không thể chia cho 0!

# b) Sửa đoạn code để xử lý lỗi khi người dùng nhập không phải là số
def square_input():
    try:
        n = int(input("Nhập một số: "))
        print(f"Bình phương của {n} là {n**2}")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")

# Để chạy hàm, bỏ comment dòng dưới
# square_input()

# c) Viết code để mở và đọc một file, sử dụng try/except để xử lý trường hợp file không tồn tại
def read_file_safely(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Lỗi: File '{filename}' không tồn tại!")
        return None

# Kiểm tra hàm
content = read_file_safely("existing_file.txt")  # Giả sử file này không tồn tại
if content:
    print("Nội dung file:", content)

# CÂU HỎI 2:
# a) Viết một đoạn code để chuyển đổi một chuỗi thành số và thực hiện phép chia
def convert_and_divide(string_value, divisor_string):
    try:
        number = float(string_value)
        divisor = float(divisor_string)
        result = number / divisor
        return result
    except ValueError:
        print("Lỗi: Không thể chuyển đổi chuỗi thành số!")
        return None
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None

# Kiểm tra hàm
print(convert_and_divide("10", "2"))  # 5.0
print(convert_and_divide("abc", "2"))  # Lỗi: Không thể chuyển đổi chuỗi thành số!
print(convert_and_divide("10", "0"))  # Lỗi: Không thể chia cho 0!

# b) Sửa đoạn code để xử lý các loại lỗi khác nhau
def process_file_content():
    try:
        filename = input("Nhập tên file: ")
        with open(filename, 'r') as file:
            content = file.read()
            number = int(content)
            result = 100 / number
            print(f"Kết quả: {result}")
    except FileNotFoundError:
        print(f"Lỗi: File '{filename}' không tồn tại!")
    except ValueError:
        print("Lỗi: Nội dung file không phải là số nguyên hợp lệ!")
    except ZeroDivisionError:
        print("Lỗi: Số trong file là 0, không thể chia cho 0!")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

# Để chạy hàm, bỏ comment dòng dưới
# process_file_content()

# CÂU HỎI 3:
# a) Viết code để nhập một số từ người dùng, sử dụng đầy đủ try, except, else, finally
def process_input():
    try:
        user_input = input("Nhập một số nguyên: ")
        number = int(user_input)
    except ValueError:
        print("Lỗi: Input không phải là số nguyên hợp lệ!")
    else:
        square = number ** 2
        print(f"Bình phương của {number} là {square}")
    finally:
        print("Kết thúc xử lý input")

# Để chạy hàm, bỏ comment dòng dưới
# process_input()

# b) Viết code để mở, đọc và xử lý một file, sử dụng đầy đủ try, except, else, finally
def process_file(filename):
    file = None
    try:
        file = open(filename, 'r', encoding='utf-8')
        content = file.read()
    except FileNotFoundError:
        print(f"Lỗi: File '{filename}' không tồn tại!")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
    else:
        word_count = len(content.split())
        print(f"File '{filename}' có {word_count} từ.")
        return content
    finally:
        if file is not None and not file.closed:
            file.close()
            print(f"File '{filename}' đã được đóng.")

# Kiểm tra hàm
process_file("sample.txt")  # Giả sử file này không tồn tại

# CÂU HỎI 4:
# a) và b) Tạo custom exception và hàm validate_age
class InvalidAgeError(Exception):
    """Exception raised when age is outside valid range."""
    pass

def validate_age(age):
    try:
        age = float(age)  # Thử chuyển đổi sang số
    except (ValueError, TypeError):
        raise TypeError("Tuổi phải là một số!")
    
    if age < 0 or age > 120:
        raise InvalidAgeError("Tuổi phải nằm trong khoảng từ 0 đến 120!")
    
    if 0 <= age < 18:
        print("Bạn chưa đủ tuổi trưởng thành")
    else:  # 18 <= age <= 120
        print("Bạn đã đủ tuổi trưởng thành")

# c) Gọi hàm validate_age với các giá trị khác nhau và xử lý các exceptions
def test_age_validation():
    test_cases = [17, 18, 150, -5, "abc", 30]
    
    for age in test_cases:
        try:
            print(f"Kiểm tra tuổi: {age}")
            validate_age(age)
        except TypeError as e:
            print(f"Lỗi kiểu dữ liệu: {e}")
        except InvalidAgeError as e:
            print(f"Lỗi giá trị tuổi: {e}")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")
        print("-" * 30)

# Chạy kiểm tra
test_age_validation()

# CÂU HỎI 5:
import logging

# a) Cấu hình logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# b) Viết hàm divide
def divide(a, b):
    try:
        # Kiểm tra kiểu dữ liệu
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            error_msg = f"Các tham số phải là số: a={a}, b={b}"
            logging.error(error_msg)
            raise TypeError(error_msg)
        
        # Kiểm tra chia cho 0
        if b == 0:
            error_msg = f"Không thể chia cho 0: a={a}, b={b}"
            logging.error(error_msg)
            raise ZeroDivisionError(error_msg)
        
        # Thực hiện phép chia
        result = a / b
        logging.info(f"Phép chia thành công: {a} / {b} = {result}")
        return result
    
    except (TypeError, ZeroDivisionError) as e:
        # Các lỗi này đã được log ở trên
        raise
    except Exception as e:
        # Log các lỗi không xác định khác
        logging.error(f"Lỗi không xác định khi chia {a} cho {b}: {e}")
        raise

# c) Gọi hàm divide với các giá trị khác nhau
def test_divide():
    test_cases = [
        (10, 2),    # Bình thường
        (10, 0),    # Chia cho 0
        ("10", 2),  # Kiểu dữ liệu không hợp lệ
        (10, "2"),  # Kiểu dữ liệu không hợp lệ
    ]
    
    for a, b in test_cases:
        try:
            print(f"Chia {a} cho {b}: ", end="")
            result = divide(a, b)
            print(f"Kết quả = {result}")
        except ZeroDivisionError:
            print("Lỗi chia cho 0!")
        except TypeError:
            print("Lỗi kiểu dữ liệu!")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

# Chạy kiểm tra
test_divide()

# BÀI TẬP NÂNG CAO 1:
import logging
import random
import time

# Cấu hình logging nếu chưa được cấu hình
if not logging.getLogger().handlers:
    logging.basicConfig(
        filename='database.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

class DatabaseConnection:
    def __init__(self, host="localhost", username="root", password="password"):
        self.host = host
        self.username = username
        self.password = password
        self.connection = None
        self.connected = False
    
    def connect(self):
        """Mô phỏng kết nối đến cơ sở dữ liệu."""
        logging.info(f"Đang kết nối đến {self.host} với username {self.username}")
        
        # Mô phỏng lỗi kết nối ngẫu nhiên (20% khả năng)
        if random.random() < 0.2:
            error_msg = f"Không thể kết nối đến {self.host}"
            logging.error(error_msg)
            raise ConnectionError(error_msg)
        
        # Mô phỏng thời gian kết nối
        time.sleep(0.5)
        self.connected = True
        self.connection = f"Connection to {self.host}"
        logging.info(f"Đã kết nối thành công đến {self.host}")
        return self.connection
    
    def execute_query(self, query):
        """Mô phỏng thực thi truy vấn SQL."""
        if not self.connected:
            error_msg = "Không thể thực thi truy vấn: Chưa kết nối đến cơ sở dữ liệu"
            logging.error(error_msg)
            raise ConnectionError(error_msg)
        
        logging.info(f"Đang thực thi truy vấn: {query}")
        
        # Kiểm tra cú pháp SQL đơn giản
        if not query.strip().lower().startswith(('select', 'insert', 'update', 'delete', 'create', 'drop', 'alter')):
            error_msg = f"Lỗi cú pháp SQL: {query}"
            logging.error(error_msg)
            raise SyntaxError(error_msg)
        
        # Mô phỏng lỗi giá trị ngẫu nhiên (10% khả năng)
        if random.random() < 0.1:
            error_msg = f"Lỗi giá trị trong truy vấn: {query}"
            logging.error(error_msg)
            raise ValueError(error_msg)
        
        # Mô phỏng thời gian thực thi
        time.sleep(0.3)
        
        # Mô phỏng kết quả trả về
        if query.strip().lower().startswith('select'):
            result = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
            logging.info(f"Truy vấn thành công, trả về {len(result)} kết quả")
            return result
        else:
            affected_rows = random.randint(1, 10)
            logging.info(f"Truy vấn thành công, {affected_rows} dòng bị ảnh hưởng")
            return affected_rows
    
    def close(self):
        """Đóng kết nối đến cơ sở dữ liệu."""
        if self.connected:
            logging.info(f"Đang đóng kết nối đến {self.host}")
            # Mô phỏng thời gian đóng kết nối
            time.sleep(0.2)
            self.connected = False
            self.connection = None
            logging.info(f"Đã đóng kết nối đến {self.host}")

# Hàm sử dụng DatabaseConnection với xử lý lỗi đầy đủ
def execute_database_operation(query):
    db = DatabaseConnection()
    try:
        db.connect()
        result = db.execute_query(query)
        print(f"Kết quả truy vấn: {result}")
        return result
    except ConnectionError as e:
        print(f"Lỗi kết nối: {e}")
    except SyntaxError as e:
        print(f"Lỗi cú pháp SQL: {e}")
    except ValueError as e:
        print(f"Lỗi giá trị: {e}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        logging.exception("Lỗi không xác định khi thực hiện thao tác cơ sở dữ liệu")
    finally:
        db.close()

# Kiểm tra với các truy vấn khác nhau
def test_database_operations():
    queries = [
        "SELECT * FROM users",
        "INSERT INTO users (name, email) VALUES ('John', 'john@example.com')",
        "INVALID QUERY",
        "UPDATE users SET status = 'active'",
    ]
    
    for query in queries:
        print(f"\nThực thi: {query}")
        execute_database_operation(query)

# Chạy kiểm tra
# test_database_operations()

# BÀI TẬP NÂNG CAO 2:
class InsufficientFundsError(Exception):
    """Exception raised when attempting to withdraw more money than available."""
    pass

class InvalidAmountError(Exception):
    """Exception raised when attempting to use an invalid amount in a transaction."""
    pass

class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        
        if initial_balance < 0:
            raise InvalidAmountError("Số dư ban đầu không được âm")
        self.balance = initial_balance
        
        print(f"Tài khoản {account_number} của {owner_name} đã được tạo với số dư {initial_balance}")
    
    def deposit(self, amount):
        """Thêm tiền vào tài khoản."""
        if amount <= 0:
            raise InvalidAmountError("Số tiền gửi phải lớn hơn 0")
        
        self.balance += amount
        print(f"Đã gửi {amount} vào tài khoản {self.account_number}. Số dư mới: {self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        """Rút tiền từ tài khoản."""
        if amount <= 0:
            raise InvalidAmountError("Số tiền rút phải lớn hơn 0")
        
        if amount > self.balance:
            raise InsufficientFundsError(f"Số dư không đủ. Số dư hiện tại: {self.balance}, Số tiền cần rút: {amount}")
        
        self.balance -= amount
        print(f"Đã rút {amount} từ tài khoản {self.account_number}. Số dư mới: {self.balance}")
        return amount
    
    def transfer(self, target_account, amount):
        """Chuyển tiền sang tài khoản khác."""
        try:
            # Rút tiền từ tài khoản nguồn
            self.withdraw(amount)
            
            # Gửi tiền vào tài khoản đích
            target_account.deposit(amount)
            
            print(f"Đã chuyển {amount} từ tài khoản {self.account_number} sang tài khoản {target_account.account_number}")
            return True
        except (InvalidAmountError, InsufficientFundsError) as e:
            print(f"Lỗi khi chuyển tiền: {e}")
            return False
    
    def __str__(self):
        return f"Tài khoản {self.account_number} - {self.owner_name}: Số dư {self.balance}"

# Hàm kiểm tra các tính năng của BankAccount
def test_bank_accounts():
    try:
        # Tạo các tài khoản
        account1 = BankAccount("1001", "Nguyễn Văn A", 1000)
        account2 = BankAccount("1002", "Trần Thị B", 500)
        
        # Thử tạo tài khoản với số dư âm
        try:
            invalid_account = BankAccount("1003", "Lê Văn C", -100)
        except InvalidAmountError as e:
            print(f"Không thể tạo tài khoản: {e}")
        
        print("\n--- Thông tin tài khoản ---")
        print(account1)
        print(account2)
        
        print("\n--- Gửi tiền ---")
        try:
            account1.deposit(500)
        except InvalidAmountError as e:
            print(f"Lỗi khi gửi tiền: {e}")
        
        try:
            account1.deposit(-100)  # Lỗi: số tiền âm
        except InvalidAmountError as e:
            print(f"Lỗi khi gửi tiền: {e}")
        
        print("\n--- Rút tiền ---")
        try:
            account1.withdraw(300)
        except (InvalidAmountError, InsufficientFundsError) as e:
            print(f"Lỗi khi rút tiền: {e}")
        
        try:
            account2.withdraw(1000)  # Lỗi: số dư không đủ
        except (InvalidAmountError, InsufficientFundsError) as e:
            print(f"Lỗi khi rút tiền: {e}")
        
        print("\n--- Chuyển tiền ---")
        account1.transfer(account2, 200)
        account1.transfer(account2, 2000)  # Lỗi: số dư không đủ
        
        print("\n--- Thông tin tài khoản sau các giao dịch ---")
        print(account1)
        print(account2)
        
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

# Chạy kiểm tra
# test_bank_accounts()
'''
