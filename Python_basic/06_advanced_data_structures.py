"""
PHẦN 6: CẤU TRÚC DỮ LIỆU NÂNG CAO TRONG PYTHON
===========================================

Bài tập từ cơ bản đến nâng cao để luyện tập về cấu trúc dữ liệu nâng cao trong Python.
"""

# CÂU HỎI 1: List comprehensions
# a) Tạo một list chứa bình phương của các số từ 1 đến 10
# b) Tạo một list chứa các số chia hết cho 3 trong khoảng từ 1 đến 50
# c) Tạo một list chứa các cặp (x, y) với x từ 1 đến 3 và y từ 1 đến 3

# Code của bạn ở đây:



# CÂU HỎI 2: Dictionary comprehensions
# a) Tạo một dictionary với key là các số từ 1 đến 10, value là bình phương của key
# b) Cho list ['apple', 'banana', 'orange'], tạo dictionary với key là từng phần tử, value là độ dài của phần tử
# c) Tạo dictionary từ hai lists: keys = ['a', 'b', 'c'] và values = [1, 2, 3]

# Code của bạn ở đây:



# CÂU HỎI 3: Set comprehensions
# a) Tạo một set chứa bình phương của các số từ 1 đến 10
# b) Tạo một set chứa các ký tự trong chuỗi "hello world"
# c) Tạo một set chứa các số chia hết cho cả 2 và 3 trong khoảng từ 1 đến 50

# Code của bạn ở đây:



# CÂU HỎI 4: Generator expressions
# a) Tạo một generator expression để tính tổng bình phương của các số từ 1 đến 100
# b) Tạo một generator expression để lọc các số chẵn từ 1 đến 20
# c) So sánh bộ nhớ sử dụng giữa list comprehension và generator expression khi xử lý dữ liệu lớn

# Code của bạn ở đây:



# CÂU HỎI 5: Collections module
# a) Sử dụng Counter để đếm tần suất xuất hiện của các phần tử trong list [1, 2, 3, 1, 2, 1, 4, 5]
# b) Sử dụng defaultdict để nhóm các từ theo chữ cái đầu tiên từ một danh sách từ
# c) Sử dụng namedtuple để tạo kiểu dữ liệu Point với thuộc tính x, y
# d) Sử dụng OrderedDict để tạo từ điển có thứ tự (Python < 3.7)
# e) Sử dụng deque để tạo một hàng đợi hai đầu và thực hiện các thao tác cơ bản

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 1:
# Viết chương trình phân tích văn bản:
# a) Đếm tần suất xuất hiện của từng từ
# b) Tìm 10 từ xuất hiện nhiều nhất
# c) Tìm các từ có độ dài lớn hơn 5 ký tự
# d) Tạo từ điển với key là độ dài từ, value là danh sách các từ có độ dài đó
# Sử dụng các kỹ thuật comprehension và collections module

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 2:
# Viết chương trình quản lý thư viện sách:
# a) Tạo namedtuple Book với các thuộc tính: id, title, author, year, status (available/borrowed)
# b) Tạo các hàm: thêm sách, mượn sách, trả sách, tìm kiếm sách theo tên/tác giả
# c) Sử dụng defaultdict để nhóm sách theo tác giả
# d) Sử dụng Counter để thống kê số lượng sách theo năm xuất bản
# e) Sử dụng list comprehension để lọc sách theo điều kiện (ví dụ: sách có sẵn, sách của tác giả cụ thể)

# Code của bạn ở đây:



# BÀI TẬP NÂNG CAO 3:
# Viết chương trình mô phỏng hệ thống cache đơn giản:
# a) Sử dụng OrderedDict để tạo một LRU cache (Least Recently Used)
# b) Cache có kích thước tối đa (ví dụ: 5 phần tử)
# c) Khi cache đầy, phần tử ít được sử dụng nhất sẽ bị loại bỏ
# d) Viết các hàm: get(key), put(key, value), display_cache()
# e) Thử nghiệm với một số trường hợp để kiểm tra tính đúng đắn

# Code của bạn ở đây:


"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
# a) List bình phương từ 1-10
binh_phuong = [x**2 for x in range(1, 11)]
print(f"Bình phương từ 1-10: {binh_phuong}")

# b) List các số chia hết cho 3 từ 1-50
chia_het_cho_3 = [x for x in range(1, 51) if x % 3 == 0]
print(f"Các số chia hết cho 3 từ 1-50: {chia_het_cho_3}")

# c) List các cặp (x, y)
cap_xy = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(f"Các cặp (x, y): {cap_xy}")

# CÂU HỎI 2:
# a) Dictionary với key là số, value là bình phương
dict_binh_phuong = {x: x**2 for x in range(1, 11)}
print(f"Dictionary bình phương: {dict_binh_phuong}")

# b) Dictionary với key là từ, value là độ dài
fruits = ['apple', 'banana', 'orange']
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(f"Dictionary độ dài từ: {fruit_lengths}")

# c) Dictionary từ hai lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {keys[i]: values[i] for i in range(len(keys))}
print(f"Dictionary từ hai lists: {combined_dict}")

# CÂU HỎI 3:
# a) Set bình phương từ 1-10
set_binh_phuong = {x**2 for x in range(1, 11)}
print(f"Set bình phương: {set_binh_phuong}")

# b) Set các ký tự trong chuỗi
char_set = {c for c in "hello world" if not c.isspace()}
print(f"Set các ký tự: {char_set}")

# c) Set các số chia hết cho cả 2 và 3
set_chia_het = {x for x in range(1, 51) if x % 2 == 0 and x % 3 == 0}
print(f"Set các số chia hết cho cả 2 và 3: {set_chia_het}")

# CÂU HỎI 4:
import sys
import time

# a) Generator expression tính tổng bình phương
gen_binh_phuong = (x**2 for x in range(1, 101))
tong_binh_phuong = sum(gen_binh_phuong)
print(f"Tổng bình phương từ 1-100: {tong_binh_phuong}")

# b) Generator expression lọc số chẵn
gen_chan = (x for x in range(1, 21) if x % 2 == 0)
so_chan = list(gen_chan)
print(f"Các số chẵn từ 1-20: {so_chan}")

# c) So sánh bộ nhớ
def compare_memory():
    # Số lượng phần tử lớn
    n = 10**6
    
    # Đo thời gian và bộ nhớ cho list comprehension
    start_time = time.time()
    list_comp = [x for x in range(n)]
    list_comp_size = sys.getsizeof(list_comp)
    list_comp_time = time.time() - start_time
    
    # Đo thời gian và bộ nhớ cho generator expression
    start_time = time.time()
    gen_exp = (x for x in range(n))
    gen_exp_size = sys.getsizeof(gen_exp)
    gen_exp_time = time.time() - start_time
    
    print("\nSo sánh bộ nhớ và thời gian cho n =", n)
    print(f"List comprehension: {list_comp_size} bytes, {list_comp_time:.6f} giây")
    print(f"Generator expression: {gen_exp_size} bytes, {gen_exp_time:.6f} giây")
    print(f"Tỉ lệ bộ nhớ (list/gen): {list_comp_size / gen_exp_size:.2f} lần")

compare_memory()

# CÂU HỎI 5:
from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

# a) Sử dụng Counter
numbers = [1, 2, 3, 1, 2, 1, 4, 5]
counter = Counter(numbers)
print(f"\nĐếm tần suất: {counter}")
print(f"Phần tử phổ biến nhất: {counter.most_common(1)}")

# b) Sử dụng defaultdict
words = ["apple", "banana", "apricot", "cherry", "blueberry", "avocado"]
grouped_words = defaultdict(list)

for word in words:
    first_letter = word[0]
    grouped_words[first_letter].append(word)

print("\nNhóm từ theo chữ cái đầu:")
for letter, words_list in grouped_words.items():
    print(f"{letter}: {words_list}")

# c) Sử dụng namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(f"\nPoint: {p}")
print(f"x = {p.x}, y = {p.y}")
print(f"Khoảng cách từ gốc tọa độ: {(p.x**2 + p.y**2)**0.5}")

# d) Sử dụng OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(f"\nOrderedDict: {ordered_dict}")

# e) Sử dụng deque
d = deque([1, 2, 3])
print(f"\nDeque ban đầu: {d}")

# Thêm phần tử
d.append(4)  # Thêm vào bên phải
d.appendleft(0)  # Thêm vào bên trái
print(f"Sau khi thêm: {d}")

# Xóa phần tử
right = d.pop()  # Xóa từ bên phải
left = d.popleft()  # Xóa từ bên trái
print(f"Sau khi xóa: {d}")
print(f"Phần tử đã xóa: bên trái = {left}, bên phải = {right}")

# Xoay deque
d.rotate(1)  # Xoay sang phải 1 vị trí
print(f"Sau khi xoay phải: {d}")
d.rotate(-2)  # Xoay sang trái 2 vị trí
print(f"Sau khi xoay trái: {d}")

# BÀI TẬP NÂNG CAO 1:
import string
from collections import Counter, defaultdict

def analyze_text(text):
    # Tiền xử lý văn bản
    text = text.lower()
    # Loại bỏ dấu câu
    for char in string.punctuation:
        text = text.replace(char, ' ')
    
    # Tách văn bản thành các từ
    words = text.split()
    
    # a) Đếm tần suất xuất hiện của từng từ
    word_counts = Counter(words)
    print("\nTần suất xuất hiện của từng từ:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
    
    # b) Tìm 10 từ xuất hiện nhiều nhất
    most_common = word_counts.most_common(10)
    print("\n10 từ xuất hiện nhiều nhất:")
    for word, count in most_common:
        print(f"{word}: {count}")
    
    # c) Tìm các từ có độ dài lớn hơn 5 ký tự
    long_words = [word for word in words if len(word) > 5]
    unique_long_words = set(long_words)
    print("\nCác từ có độ dài > 5 ký tự:")
    print(unique_long_words)
    
    # d) Tạo từ điển với key là độ dài từ, value là danh sách các từ có độ dài đó
    words_by_length = defaultdict(set)
    for word in words:
        words_by_length[len(word)].add(word)
    
    print("\nTừ điển nhóm từ theo độ dài:")
    for length, word_set in sorted(words_by_length.items()):
        print(f"Độ dài {length}: {word_set}")
    
    return {
        'word_counts': word_counts,
        'most_common': most_common,
        'long_words': unique_long_words,
        'words_by_length': words_by_length
    }

# Thử nghiệm với một đoạn văn bản
sample_text = """
Python is a programming language that lets you work quickly and integrate systems more effectively.
Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.
Python is a great first language to learn because it's easy to understand and fun to use!
"""

analysis_result = analyze_text(sample_text)

# BÀI TẬP NÂNG CAO 2:
from collections import namedtuple, defaultdict, Counter

# a) Tạo namedtuple Book
Book = namedtuple('Book', ['id', 'title', 'author', 'year', 'status'])

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, id, title, author, year):
        """Thêm sách mới vào thư viện"""
        # Kiểm tra xem ID đã tồn tại chưa
        if any(book.id == id for book in self.books):
            print(f"Sách với ID {id} đã tồn tại!")
            return False
        
        book = Book(id=id, title=title, author=author, year=year, status='available')
        self.books.append(book)
        print(f"Đã thêm sách: {title} bởi {author}")
        return True
    
    def borrow_book(self, id):
        """Mượn sách theo ID"""
        for i, book in enumerate(self.books):
            if book.id == id:
                if book.status == 'available':
                    # Tạo sách mới với status = 'borrowed'
                    updated_book = Book(id=book.id, title=book.title, 
                                        author=book.author, year=book.year, 
                                        status='borrowed')
                    self.books[i] = updated_book
                    print(f"Đã mượn sách: {book.title}")
                    return True
                else:
                    print(f"Sách {book.title} hiện không có sẵn!")
                    return False
        
        print(f"Không tìm thấy sách với ID {id}!")
        return False
    
    def return_book(self, id):
        """Trả sách theo ID"""
        for i, book in enumerate(self.books):
            if book.id == id:
                if book.status == 'borrowed':
                    # Tạo sách mới với status = 'available'
                    updated_book = Book(id=book.id, title=book.title, 
                                        author=book.author, year=book.year, 
                                        status='available')
                    self.books[i] = updated_book
                    print(f"Đã trả sách: {book.title}")
                    return True
                else:
                    print(f"Sách {book.title} chưa được mượn!")
                    return False
        
        print(f"Không tìm thấy sách với ID {id}!")
        return False
    
    def search_by_title(self, title):
        """Tìm kiếm sách theo tên (tìm kiếm mờ)"""
        title = title.lower()
        results = [book for book in self.books if title in book.title.lower()]
        return results
    
    def search_by_author(self, author):
        """Tìm kiếm sách theo tác giả (tìm kiếm mờ)"""
        author = author.lower()
        results = [book for book in self.books if author in book.author.lower()]
        return results
    
    def group_by_author(self):
        """Nhóm sách theo tác giả"""
        grouped = defaultdict(list)
        for book in self.books:
            grouped[book.author].append(book)
        return grouped
    
    def count_by_year(self):
        """Thống kê số lượng sách theo năm xuất bản"""
        return Counter(book.year for book in self.books)
    
    def filter_books(self, status=None, author=None, year=None):
        """Lọc sách theo điều kiện"""
        filtered = self.books
        
        if status:
            filtered = [book for book in filtered if book.status == status]
        
        if author:
            filtered = [book for book in filtered if author.lower() in book.author.lower()]
        
        if year:
            filtered = [book for book in filtered if book.year == year]
        
        return filtered
    
    def display_books(self, books=None):
        """Hiển thị danh sách sách"""
        if books is None:
            books = self.books
        
        if not books:
            print("Không có sách nào để hiển thị!")
            return
        
        print(f"\n{'ID':<5}{'Tên sách':<30}{'Tác giả':<20}{'Năm':<6}{'Trạng thái':<10}")
        print("-" * 71)
        
        for book in books:
            print(f"{book.id:<5}{book.title:<30}{book.author:<20}{book.year:<6}{book.status:<10}")

# Thử nghiệm thư viện
def test_library():
    lib = Library()
    
    # Thêm sách
    lib.add_book("B001", "Python Programming", "John Smith", 2020)
    lib.add_book("B002", "Data Science with Python", "Jane Doe", 2019)
    lib.add_book("B003", "Machine Learning Basics", "John Smith", 2021)
    lib.add_book("B004", "Web Development with Django", "Alice Johnson", 2020)
    lib.add_book("B005", "Python for Beginners", "Bob Brown", 2018)
    
    # Hiển thị tất cả sách
    print("\nTất cả sách trong thư viện:")
    lib.display_books()
    
    # Mượn sách
    lib.borrow_book("B001")
    lib.borrow_book("B003")
    
    # Tìm kiếm sách
    print("\nKết quả tìm kiếm với từ khóa 'Python':")
    results = lib.search_by_title("Python")
    lib.display_books(results)
    
    # Nhóm sách theo tác giả
    print("\nSách nhóm theo tác giả:")
    by_author = lib.group_by_author()
    for author, books in by_author.items():
        print(f"\nTác giả: {author}")
        lib.display_books(books)
    
    # Thống kê theo năm
    print("\nThống kê sách theo năm:")
    year_counts = lib.count_by_year()
    for year, count in sorted(year_counts.items()):
        print(f"Năm {year}: {count} cuốn")
    
    # Lọc sách có sẵn
    print("\nSách có sẵn:")
    available_books = lib.filter_books(status="available")
    lib.display_books(available_books)
    
    # Lọc sách của tác giả John Smith
    print("\nSách của John Smith:")
    smith_books = lib.filter_books(author="John Smith")
    lib.display_books(smith_books)
    
    # Trả sách
    lib.return_book("B001")
    
    # Hiển thị lại tất cả sách
    print("\nTất cả sách sau khi cập nhật:")
    lib.display_books()

# Chạy thử nghiệm
# test_library()

# BÀI TẬP NÂNG CAO 3:
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        """Khởi tạo cache với kích thước tối đa"""
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        """
        Lấy giá trị từ cache theo key.
        Nếu key tồn tại, di chuyển item lên đầu (recently used).
        """
        if key not in self.cache:
            return -1
        
        # Di chuyển item lên đầu bằng cách xóa và thêm lại
        value = self.cache.pop(key)
        self.cache[key] = value
        return value
    
    def put(self, key, value):
        """
        Thêm hoặc cập nhật giá trị vào cache.
        Nếu key đã tồn tại, cập nhật giá trị và di chuyển lên đầu.
        Nếu cache đầy, xóa item ít được sử dụng nhất (đầu OrderedDict).
        """
        # Nếu key đã tồn tại, xóa nó trước
        if key in self.cache:
            self.cache.pop(key)
        # Nếu cache đầy, xóa item đầu tiên (least recently used)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        
        # Thêm item mới vào cuối (most recently used)
        self.cache[key] = value
    
    def display_cache(self):
        """Hiển thị trạng thái hiện tại của cache"""
        print("\nLRU Cache (Least Recently Used -> Most Recently Used):")
        if not self.cache:
            print("Cache trống!")
            return
        
        for key, value in self.cache.items():
            print(f"{key}: {value}")

# Thử nghiệm LRU Cache
def test_lru_cache():
    # Tạo cache với kích thước 3
    cache = LRUCache(3)
    
    # Thêm các phần tử
    cache.put(1, "One")
    cache.display_cache()
    
    cache.put(2, "Two")
    cache.display_cache()
    
    cache.put(3, "Three")
    cache.display_cache()
    
    # Cache đầy, truy cập phần tử 1 để đưa nó lên đầu danh sách MRU
    print(f"\nLấy giá trị của key 1: {cache.get(1)}")
    cache.display_cache()
    
    # Thêm phần tử mới khi cache đã đầy
    cache.put(4, "Four")  # Phần tử 2 sẽ bị loại bỏ (LRU)
    print("\nSau khi thêm key 4:")
    cache.display_cache()
    
    # Truy cập phần tử không tồn tại
    print(f"\nLấy giá trị của key 2 (đã bị loại bỏ): {cache.get(2)}")
    
    # Cập nhật giá trị của phần tử đã tồn tại
    cache.put(3, "THREE-UPDATED")
    print("\nSau khi cập nhật key 3:")
    cache.display_cache()
    
    # Thêm phần tử mới
    cache.put(5, "Five")  # Phần tử 4 sẽ bị loại bỏ (LRU)
    print("\nSau khi thêm key 5:")
    cache.display_cache()

# Chạy thử nghiệm
# test_lru_cache()
"""

