# Library Management System

Ứng dụng Django quản lý thư viện với các model cơ bản.

## Cấu trúc Model

### 1. Các Model chính:
- **Author** - Quản lý thông tin tác giả
- **Publisher** - Quản lý thông tin nhà xuất bản  
- **Category** - Phân loại sách
- **Book** - Thông tin chi tiết về sách
- **Member** - Thông tin độc giả/thành viên
- **Staff** - Thông tin nhân viên thư viện
- **Borrowing** - Phiếu mượn sách
- **BorrowingDetail** - Chi tiết sách trong phiếu mượn
- **Fine** - Quản lý tiền phạt
- **Log** - Nhật ký hoạt động

### 2. Mối quan hệ:
- Một **Book** thuộc một **Author**, **Publisher**, **Category**
- Một **Borrowing** thuộc một **Member**
- Một **BorrowingDetail** liên kết **Borrowing** và **Book**
- Một **Fine** thuộc một **Borrowing**

## Cài đặt

1. Tạo migration:
```bash
python manage.py makemigrations library
```

2. Áp dụng migration:
```bash
python manage.py migrate
```

3. Sử dụng Django Admin để quản lý dữ liệu:
```bash
python manage.py createsuperuser
python manage.py runserver
```

Truy cập: http://localhost:8000/admin/

## Lưu ý
- App này chỉ chứa định nghĩa model cơ bản
- Để sử dụng đầy đủ tính năng, cần thêm views, templates và logic nghiệp vụ
