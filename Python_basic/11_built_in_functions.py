"""
PHẦN 11: BUILT-IN FUNCTIONS TRONG PYTHON
=========================================

Bài tập từ cơ bản đến nâng cao để luyện tập về các hàm built-in trong Python.
"""

# CÂU HỎI 1: Map, filter, reduce
# a) Sử dụng map() để chuyển đổi một list các số thành bình phương của chúng
# b) Sử dụng filter() để lọc ra các số chẵn từ một list
# c) Sử dụng reduce() để tính tổng của một list các số
# d) Kết hợp map() và filter() để tính bình phương của các số lẻ trong list

# Code của bạn ở đây:




# CÂU HỎI 2: Zip, enumerate
# a) Sử dụng zip() để ghép hai list thành một list các tuple
# b) Sử dụng enumerate() để in ra chỉ số và giá trị của mỗi phần tử trong list
# c) Sử dụng zip() với 3 list khác nhau
# d) Sử dụng zip() và dict() để tạo dictionary từ hai list

# Code của bạn ở đây:




# CÂU HỎI 3: Any, all
# a) Sử dụng any() để kiểm tra xem trong list có số nào lớn hơn 10 không
# b) Sử dụng all() để kiểm tra xem tất cả các số trong list có dương không
# c) Kết hợp any(), all() với list comprehension để kiểm tra tính chất của list
# d) Viết một hàm sử dụng any() để kiểm tra xem một chuỗi có chứa ký tự đặc biệt không

# Code của bạn ở đây:




# CÂU HỎI 4: Sorted, reversed
# a) Sử dụng sorted() để sắp xếp một list các số theo thứ tự tăng dần
# b) Sử dụng sorted() với tham số reverse=True để sắp xếp giảm dần
# c) Sử dụng sorted() với key function để sắp xếp một list các chuỗi theo độ dài
# d) Sử dụng reversed() để đảo ngược một list và chuyển kết quả thành list mới

# Code của bạn ở đây:




# CÂU HỎI 5: Các hàm built-in khác
# a) Sử dụng sum() để tính tổng các số trong list
# b) Sử dụng min() và max() để tìm giá trị nhỏ nhất và lớn nhất trong list
# c) Sử dụng round() để làm tròn số thực đến 2 chữ số thập phân
# d) Sử dụng isinstance() để kiểm tra kiểu dữ liệu của một biến

# Code của bạn ở đây:




# BÀI TẬP NÂNG CAO 1:
# Viết một chương trình xử lý dữ liệu sử dụng các hàm built-in:
# - Cho một list các dictionary chứa thông tin về sản phẩm (tên, giá, số lượng)
# - Sử dụng map() để tính tổng giá trị của mỗi sản phẩm (giá * số lượng)
# - Sử dụng filter() để lọc ra các sản phẩm có giá trị trên 1000
# - Sử dụng sorted() để sắp xếp các sản phẩm theo tổng giá trị giảm dần
# - Sử dụng reduce() để tính tổng giá trị của tất cả sản phẩm

# Code của bạn ở đây:




# BÀI TẬP NÂNG CAO 2:
# Viết một chương trình phân tích văn bản:
# - Đọc một file văn bản
# - Sử dụng map() để chuyển tất cả các từ thành chữ thường
# - Sử dụng filter() để loại bỏ các từ stopwords (như "the", "a", "an", "in", etc.)
# - Sử dụng collections.Counter và sorted() để tìm 10 từ xuất hiện nhiều nhất
# - Sử dụng zip() và dict() để tạo một từ điển tần suất xuất hiện của các từ

# Code của bạn ở đây:




"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1:
# a) Sử dụng map() để chuyển đổi một list các số thành bình phương của chúng
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(f"Bình phương của {numbers}: {squares}")

# b) Sử dụng filter() để lọc ra các số chẵn từ một list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Các số chẵn trong {numbers}: {even_numbers}")

# c) Sử dụng reduce() để tính tổng của một list các số
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(f"Tổng của {numbers}: {sum_result}")

# d) Kết hợp map() và filter() để tính bình phương của các số lẻ trong list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))
print(f"Bình phương của các số lẻ trong {numbers}: {odd_squares}")

# CÂU HỎI 2:
# a) Sử dụng zip() để ghép hai list thành một list các tuple
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = list(zip(names, ages))
print(f"Ghép {names} và {ages}: {people}")

# b) Sử dụng enumerate() để in ra chỉ số và giá trị của mỗi phần tử trong list
fruits = ["apple", "banana", "cherry", "date"]
print("Danh sách fruits với chỉ số:")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# c) Sử dụng zip() với 3 list khác nhau
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]
people_info = list(zip(names, ages, cities))
print(f"Ghép 3 list: {people_info}")

# d) Sử dụng zip() và dict() để tạo dictionary từ hai list
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
person = dict(zip(keys, values))
print(f"Dictionary từ zip: {person}")

# CÂU HỎI 3:
# a) Sử dụng any() để kiểm tra xem trong list có số nào lớn hơn 10 không
numbers = [1, 5, 8, 12, 3]
has_greater_than_10 = any(x > 10 for x in numbers)
print(f"Có số nào lớn hơn 10 trong {numbers}? {has_greater_than_10}")

# b) Sử dụng all() để kiểm tra xem tất cả các số trong list có dương không
numbers1 = [1, 5, 8, 12, 3]
numbers2 = [1, 5, 0, 12, 3]
numbers3 = [1, 5, -1, 12, 3]

all_positive1 = all(x > 0 for x in numbers1)
all_positive2 = all(x > 0 for x in numbers2)
all_positive3 = all(x > 0 for x in numbers3)

print(f"Tất cả các số trong {numbers1} có dương? {all_positive1}")
print(f"Tất cả các số trong {numbers2} có dương? {all_positive2}")
print(f"Tất cả các số trong {numbers3} có dương? {all_positive3}")

# c) Kết hợp any(), all() với list comprehension để kiểm tra tính chất của list
numbers = [2, 4, 6, 8, 10]
all_even = all(x % 2 == 0 for x in numbers)
any_greater_than_5 = any(x > 5 for x in numbers)

print(f"Tất cả các số trong {numbers} đều chẵn? {all_even}")
print(f"Có số nào trong {numbers} lớn hơn 5? {any_greater_than_5}")

# d) Viết một hàm sử dụng any() để kiểm tra xem một chuỗi có chứa ký tự đặc biệt không
def has_special_char(s):
    special_chars = "!@#$%^&*()_+-=[]{}|;:'\",.<>/?\\"
    return any(char in special_chars for char in s)

test_strings = ["Hello", "Hello!", "Hello@World", "NoSpecialChars123"]
for s in test_strings:
    print(f"'{s}' có chứa ký tự đặc biệt? {has_special_char(s)}")

# CÂU HỎI 4:
# a) Sử dụng sorted() để sắp xếp một list các số theo thứ tự tăng dần
numbers = [5, 2, 8, 1, 9, 3]
sorted_numbers = sorted(numbers)
print(f"Sắp xếp tăng dần {numbers}: {sorted_numbers}")

# b) Sử dụng sorted() với tham số reverse=True để sắp xếp giảm dần
numbers = [5, 2, 8, 1, 9, 3]
sorted_desc = sorted(numbers, reverse=True)
print(f"Sắp xếp giảm dần {numbers}: {sorted_desc}")

# c) Sử dụng sorted() với key function để sắp xếp một list các chuỗi theo độ dài
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
sorted_by_length = sorted(words, key=len)
print(f"Sắp xếp theo độ dài: {sorted_by_length}")

# d) Sử dụng reversed() để đảo ngược một list và chuyển kết quả thành list mới
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(f"Đảo ngược {numbers}: {reversed_numbers}")

# CÂU HỎI 5:
# a) Sử dụng sum() để tính tổng các số trong list
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"Tổng của {numbers}: {total}")

# b) Sử dụng min() và max() để tìm giá trị nhỏ nhất và lớn nhất trong list
numbers = [5, 2, 8, 1, 9, 3]
min_value = min(numbers)
max_value = max(numbers)
print(f"Giá trị nhỏ nhất trong {numbers}: {min_value}")
print(f"Giá trị lớn nhất trong {numbers}: {max_value}")

# c) Sử dụng round() để làm tròn số thực đến 2 chữ số thập phân
value = 3.14159
rounded = round(value, 2)
print(f"Làm tròn {value} đến 2 chữ số thập phân: {rounded}")

# d) Sử dụng isinstance() để kiểm tra kiểu dữ liệu của một biến
variables = [42, "Hello", 3.14, [1, 2, 3], {"name": "Alice"}, (1, 2)]

for var in variables:
    if isinstance(var, int):
        print(f"{var} là số nguyên (int)")
    elif isinstance(var, float):
        print(f"{var} là số thực (float)")
    elif isinstance(var, str):
        print(f"{var} là chuỗi (str)")
    elif isinstance(var, list):
        print(f"{var} là list")
    elif isinstance(var, dict):
        print(f"{var} là dictionary")
    elif isinstance(var, tuple):
        print(f"{var} là tuple")
    else:
        print(f"{var} là kiểu dữ liệu khác")

# BÀI TẬP NÂNG CAO 1:
from functools import reduce

# Danh sách sản phẩm
products = [
    {"name": "Laptop", "price": 1200, "quantity": 2},
    {"name": "Phone", "price": 800, "quantity": 5},
    {"name": "Tablet", "price": 500, "quantity": 3},
    {"name": "Headphones", "price": 100, "quantity": 10},
    {"name": "Monitor", "price": 300, "quantity": 2},
    {"name": "Keyboard", "price": 50, "quantity": 5}
]

# Tính tổng giá trị của mỗi sản phẩm
def calculate_total_value(product):
    product["total_value"] = product["price"] * product["quantity"]
    return product

products_with_total = list(map(calculate_total_value, products))

# In ra sản phẩm với tổng giá trị
print("Sản phẩm với tổng giá trị:")
for product in products_with_total:
    print(f"{product['name']}: ${product['total_value']}")

# Lọc ra các sản phẩm có giá trị trên 1000
expensive_products = list(filter(lambda p: p["total_value"] > 1000, products_with_total))

print("\nSản phẩm có giá trị trên $1000:")
for product in expensive_products:
    print(f"{product['name']}: ${product['total_value']}")

# Sắp xếp sản phẩm theo tổng giá trị giảm dần
sorted_products = sorted(products_with_total, key=lambda p: p["total_value"], reverse=True)

print("\nSản phẩm sắp xếp theo giá trị giảm dần:")
for product in sorted_products:
    print(f"{product['name']}: ${product['total_value']}")

# Tính tổng giá trị của tất cả sản phẩm
total_value = reduce(lambda acc, p: acc + p["total_value"], products_with_total, 0)

print(f"\nTổng giá trị của tất cả sản phẩm: ${total_value}")

# BÀI TẬP NÂNG CAO 2:
import re
from collections import Counter
from functools import reduce

def analyze_text(file_path):
    try:
        # Đọc file văn bản
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Tiền xử lý văn bản: loại bỏ ký tự đặc biệt và chia thành các từ
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Danh sách stopwords
        stopwords = {"the", "a", "an", "in", "on", "at", "to", "for", "of", "and", 
                    "is", "are", "was", "were", "be", "been", "being", "by", "with", 
                    "that", "this", "it", "as", "from", "not", "or", "but", "which", "what"}
        
        # Chuyển tất cả các từ thành chữ thường
        lowercase_words = list(map(str.lower, words))
        
        # Loại bỏ stopwords
        filtered_words = list(filter(lambda word: word not in stopwords, lowercase_words))
        
        # Đếm tần suất xuất hiện của các từ
        word_counts = Counter(filtered_words)
        
        # Tìm 10 từ xuất hiện nhiều nhất
        most_common = word_counts.most_common(10)
        
        # Tạo từ điển tần suất xuất hiện
        words_set = sorted(set(filtered_words))
        frequencies = [word_counts[word] for word in words_set]
        frequency_dict = dict(zip(words_set, frequencies))
        
        # Hiển thị kết quả
        print(f"Tổng số từ trong văn bản: {len(words)}")
        print(f"Số từ sau khi loại bỏ stopwords: {len(filtered_words)}")
        print(f"Số từ duy nhất: {len(frequency_dict)}")
        
        print("\n10 từ xuất hiện nhiều nhất:")
        for word, count in most_common:
            print(f"{word}: {count} lần")
        
        # Tính độ dài trung bình của các từ
        avg_word_length = sum(map(len, filtered_words)) / len(filtered_words) if filtered_words else 0
        print(f"\nĐộ dài trung bình của các từ: {avg_word_length:.2f} ký tự")
        
        return {
            "total_words": len(words),
            "filtered_words": len(filtered_words),
            "unique_words": len(frequency_dict),
            "most_common": most_common,
            "frequency_dict": frequency_dict,
            "avg_word_length": avg_word_length
        }
        
    except Exception as e:
        print(f"Lỗi khi phân tích văn bản: {e}")
        return None

# Để sử dụng hàm này, tạo một file văn bản và gọi:
# result = analyze_text("sample_text.txt")
"""
