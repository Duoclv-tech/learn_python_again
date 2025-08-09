"""
PHẦN 23: CÁC CHỦ ĐỀ NÂNG CAO
=============================

Bài tập về Regular Expressions, Pickle/serialization, Socket programming,
Database connections, Web scraping.
"""

# CÂU HỎI 1: Regular expressions (re)
# a) Viết regex để trích xuất email từ chuỗi
# b) Viết regex để kiểm tra số điện thoại dạng 10 chữ số bắt đầu bằng 0
# c) Viết regex để tách các từ tiếng Anh (chỉ a-zA-Z) khỏi văn bản lẫn ký tự đặc biệt

# Code của bạn ở đây:



# CÂU HỎI 2: Pickle và serialization
# a) Dùng pickle để lưu/đọc một object (dict) ra file
# b) Dùng json để lưu/đọc một list đối tượng

# Code của bạn ở đây:



# CÂU HỎI 3: Socket programming
# a) Viết TCP echo server đơn giản (localhost:5000)
# b) Viết client gửi thông điệp và nhận echo

# Code của bạn ở đây:



# CÂU HỎI 4: Database connections
# a) Dùng sqlite3 tạo DB, tạo bảng users(id, name), chèn dữ liệu, truy vấn tất cả

# Code của bạn ở đây:



# CÂU HỎI 5: Web scraping
# a) Dùng requests + BeautifulSoup để lấy tiêu đề các bài viết từ một trang mẫu
# b) Dùng selector CSS/BeautifulSoup để lọc phần tử mong muốn

# Code của bạn ở đây:



"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

import re
import pickle
import json
import socket
import threading
import sqlite3

try:
    import requests
    from bs4 import BeautifulSoup
except Exception:
    requests = None
    BeautifulSoup = None

# CÂU HỎI 1: re
text = "Liên hệ: a@example.com, b@example.org; số 0901234567; và từ 'Hello-world'!"
emails = re.findall(r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,}", text)
phones = re.findall(r"\b0\d{9}\b", text)
words = re.findall(r"[A-Za-z]+", text)
print("Emails:", emails)
print("Phones:", phones)
print("Words:", words)

# CÂU HỎI 2: pickle/json
obj = {"name": "Alice", "age": 30, "scores": [8, 9, 10]}
with open("data.pkl", "wb") as f:
    pickle.dump(obj, f)
with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)
print("Loaded pickle:", loaded)

data = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
with open("data.json", "r", encoding="utf-8") as f:
    print("Loaded json:", json.load(f))

# CÂU HỎI 3: sockets
def echo_server(host="127.0.0.1", port=5000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    print("Server listening", (host, port))
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        conn.sendall(data)
    s.close()

def echo_client(host="127.0.0.1", port=5000, msg=b"hello"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(msg)
    data = s.recv(1024)
    s.close()
    return data

# Chạy demo echo (không kích hoạt mặc định)
# threading.Thread(target=echo_server, daemon=True).start()
# time.sleep(0.1)
# print(echo_client(msg=b"ping"))

# CÂU HỎI 4: sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
cur.executemany("INSERT INTO users(name) VALUES (?)", [("Alice",), ("Bob",)])
conn.commit()
cur.execute("SELECT * FROM users")
print("Users:", cur.fetchall())
conn.close()

# CÂU HỎI 5: Web scraping
if requests and BeautifulSoup:
    try:
        resp = requests.get("https://example.com", timeout=5)
        if resp.ok:
            soup = BeautifulSoup(resp.text, "html.parser")
            title = soup.select_one("title")
            print("Page title:", title.text.strip() if title else "N/A")
    except Exception as e:
        print("Web scraping demo skipped:", e)
else:
    print("Cần cài đặt 'requests' và 'beautifulsoup4' để chạy ví dụ web scraping")

"""

