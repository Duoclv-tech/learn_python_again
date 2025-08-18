from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Author(models.Model):
    """Model cho Tác giả"""
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Tên tác giả")
    bio = models.TextField(blank=True, null=True, verbose_name="Tiểu sử tác giả")
    
    class Meta:
        verbose_name = "Tác giả"
        verbose_name_plural = "Tác giả"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Publisher(models.Model):
    """Model cho Nhà xuất bản"""
    publisher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Tên nhà xuất bản")
    address = models.TextField(blank=True, null=True, verbose_name="Địa chỉ")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Số điện thoại")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    
    class Meta:
        verbose_name = "Nhà xuất bản"
        verbose_name_plural = "Nhà xuất bản"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Category(models.Model):
    """Model cho Thể loại sách"""
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Tên thể loại")
    
    class Meta:
        verbose_name = "Thể loại"
        verbose_name_plural = "Thể loại"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    """Model cho Thẻ tag sách"""
    name = models.CharField(max_length=50, unique=True, verbose_name="Tên tag")
    description = models.TextField(blank=True, null=True, verbose_name="Mô tả tag")
    
    class Meta:
        verbose_name = "Thẻ tag"
        verbose_name_plural = "Thẻ tag"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Book(models.Model):
    """Model cho Sách"""
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Tiêu đề sách")
    # Mối quan hệ nhiều-nhiều với Author
    authors = models.ManyToManyField(Author, verbose_name="Tác giả")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="Nhà xuất bản")
    isbn = models.CharField(max_length=20, unique=True, verbose_name="Mã ISBN")
    publication_year = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(timezone.now().year)],
        verbose_name="Năm xuất bản"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Thể loại")
    # Mối quan hệ nhiều-nhiều với Tag
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Thẻ tag")
    pages = models.PositiveIntegerField(verbose_name="Số trang")
    description = models.TextField(blank=True, null=True, verbose_name="Mô tả sách")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Số lượng sách")
    available_quantity = models.PositiveIntegerField(default=1, verbose_name="Số lượng có sẵn")
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name="Vị trí")
    
    class Meta:
        verbose_name = "Sách"
        verbose_name_plural = "Sách"
        ordering = ['title']
    
    def __str__(self):
        # Lấy tên của tất cả tác giả
        author_names = ", ".join([author.name for author in self.authors.all()])
        return f"{self.title} - {author_names}"
    
    def get_authors_display(self):
        """Trả về chuỗi tên tác giả để hiển thị"""
        return ", ".join([author.name for author in self.authors.all()])


class Member(models.Model):
    """Model cho Độc giả/Thành viên"""
    STATUS_CHOICES = [
        ('active', 'Hoạt động'),
        ('inactive', 'Khóa'),
        ('expired', 'Hết hạn'),
    ]
    
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Tên độc giả")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Số điện thoại")
    address = models.TextField(verbose_name="Địa chỉ")
    membership_date = models.DateField(auto_now_add=True, verbose_name="Ngày đăng ký")
    membership_expiry = models.DateField(verbose_name="Ngày hết hạn")
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='active',
        verbose_name="Trạng thái"
    )
    
    class Meta:
        verbose_name = "Độc giả"
        verbose_name_plural = "Độc giả"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.email}"


class Staff(models.Model):
    """Model cho Nhân viên"""
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Tên nhân viên")
    phone = models.CharField(max_length=20, verbose_name="Số điện thoại")
    address = models.TextField(verbose_name="Địa chỉ")
    position = models.CharField(max_length=100, verbose_name="Chức vụ")
    
    class Meta:
        verbose_name = "Nhân viên"
        verbose_name_plural = "Nhân viên"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.position}"


class Borrowing(models.Model):
    """Model cho Phiếu mượn sách"""
    STATUS_CHOICES = [
        ('borrowed', 'Đang mượn'),
        ('returned', 'Đã trả'),
        ('overdue', 'Quá hạn'),
    ]
    
    borrowing_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="Độc giả")
    borrow_date = models.DateField(auto_now_add=True, verbose_name="Ngày mượn")
    due_date = models.DateField(verbose_name="Ngày hẹn trả")
    return_date = models.DateField(blank=True, null=True, verbose_name="Ngày trả thực tế")
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='borrowed',
        verbose_name="Trạng thái"
    )
    fine_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00,
        verbose_name="Tiền phạt"
    )
    
    class Meta:
        verbose_name = "Phiếu mượn sách"
        verbose_name_plural = "Phiếu mượn sách"
        ordering = ['-borrow_date']
    
    def __str__(self):
        return f"Phiếu mượn #{self.borrowing_id} - {self.member.name}"


class BorrowingDetail(models.Model):
    """Model cho Chi tiết phiếu mượn"""
    STATUS_CHOICES = [
        ('borrowed', 'Chưa trả'),
        ('returned', 'Đã trả'),
    ]
    
    borrowing_detail_id = models.AutoField(primary_key=True)
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE, verbose_name="Phiếu mượn")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Sách")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Số lượng")
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='borrowed',
        verbose_name="Trạng thái"
    )
    
    class Meta:
        verbose_name = "Chi tiết phiếu mượn"
        verbose_name_plural = "Chi tiết phiếu mượn"
        unique_together = ['borrowing', 'book']
    
    def __str__(self):
        return f"{self.borrowing} - {self.book.title}"


class Fine(models.Model):
    """Model cho Phạt"""
    REASON_CHOICES = [
        ('late_return', 'Trả muộn'),
        ('lost_book', 'Mất sách'),
        ('damaged_book', 'Hư hỏng sách'),
    ]
    
    STATUS_CHOICES = [
        ('unpaid', 'Chưa thanh toán'),
        ('paid', 'Đã thanh toán'),
    ]
    
    fine_id = models.AutoField(primary_key=True)
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE, verbose_name="Phiếu mượn")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Số tiền phạt")
    reason = models.CharField(
        max_length=20, 
        choices=REASON_CHOICES, 
        verbose_name="Lý do phạt"
    )
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='unpaid',
        verbose_name="Trạng thái"
    )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo phạt")
    paid_date = models.DateTimeField(blank=True, null=True, verbose_name="Ngày thanh toán")
    
    class Meta:
        verbose_name = "Phạt"
        verbose_name_plural = "Phạt"
        ordering = ['-created_date']
    
    def __str__(self):
        return f"Phạt #{self.fine_id} - {self.borrowing.member.name} - {self.amount}đ"


class Log(models.Model):
    """Model cho Nhật ký hoạt động"""
    ACTION_CHOICES = [
        ('borrow_book', 'Mượn sách'),
        ('return_book', 'Trả sách'),
        ('add_book', 'Thêm sách'),
        ('edit_book', 'Sửa thông tin sách'),
        ('delete_book', 'Xóa sách'),
        ('add_member', 'Thêm thành viên'),
        ('edit_member', 'Sửa thông tin thành viên'),
        ('pay_fine', 'Thanh toán phạt'),
    ]
    
    log_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(verbose_name="ID người dùng")
    user_type = models.CharField(max_length=10, verbose_name="Loại người dùng")  # 'staff' hoặc 'member'
    action = models.CharField(
        max_length=20, 
        choices=ACTION_CHOICES, 
        verbose_name="Hành động"
    )
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Thời gian")
    details = models.TextField(verbose_name="Chi tiết hành động")
    
    class Meta:
        verbose_name = "Nhật ký hoạt động"
        verbose_name_plural = "Nhật ký hoạt động"
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.action} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
