"""
PHẦN 22: TESTING TRONG PYTHON
=============================

Bài tập về unittest, pytest, mock, TDD, code coverage.
"""

# CÂU HỎI 1: unittest module
# a) Viết hàm add(a, b) và unittest kiểm thử nhiều case
# b) Dùng setUp/tearDown

# Code của bạn ở đây:



# CÂU HỎI 2: pytest framework
# a) Viết các test function theo phong cách pytest cho add và một số hàm khác
# b) Dùng parametrize để kiểm thử nhiều dữ liệu

# Code của bạn ở đây:



# CÂU HỎI 3: Mock objects
# a) Dùng unittest.mock để mock hàm truy cập mạng/DB trong lúc test

# Code của bạn ở đây:



# CÂU HỎI 4: Test-driven development (TDD)
# a) Viết yêu cầu cho hàm format_name(first, last) -> 'Last, First'
# b) Viết test trước rồi implement cho pass test

# Code của bạn ở đây:



# CÂU HỎI 5: Code coverage
# a) Hướng dẫn chạy coverage: coverage run -m pytest; coverage html
# b) Viết một test suite đủ bao phủ các nhánh

# Ghi chú của bạn ở đây:



"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

import unittest
from unittest.mock import patch

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.data = [(1, 2, 3), (0, 0, 0), (-1, 1, 0)]

    def tearDown(self):
        self.data = None

    def test_add_cases(self):
        for a, b, expected in self.data:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)

def format_name(first: str, last: str) -> str:
    return f"{last}, {first}"

class TestFormatName(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(format_name("John", "Doe"), "Doe, John")
    def test_trim(self):
        self.assertEqual(format_name("  Ada ", "  Lovelace ").replace(" ", ""), "Lovelace,Ada")

def get_remote_data():
    # giả lập gọi mạng/DB
    raise RuntimeError("Network not allowed in tests")

def process():
    data = get_remote_data()
    return data.upper()

class TestMock(unittest.TestCase):
    @patch(__name__ + '.get_remote_data', return_value='ok')
    def test_process(self, mock_get):
        self.assertEqual(process(), 'OK')
        mock_get.assert_called_once()

if __name__ == '__main__':
    unittest.main(exit=False)

# Pytest gợi ý (tạo file test_*.py riêng khi dùng pytest):
pytest_note = """
Ví dụ pytest:

import pytest
from module import add

@pytest.mark.parametrize('a,b,expected', [(1,2,3),(0,0,0),(-1,1,0)])
def test_add(a,b,expected):
    assert add(a,b) == expected

Chạy:
pytest -q
coverage run -m pytest && coverage html
"""
print(pytest_note)

