from django.db import transaction
from django.db.models import Q, Count
from django.utils import timezone
from datetime import timedelta
from .models import Book, Member, Borrowing, BorrowingDetail, Fine, Log


class LibraryManager:
    """Lớp quản lý các tác vụ thông thường của thư viện"""
    
    @staticmethod
    def borrow_book(member_id, book_ids, days=14):
        """
        Cho mượn sách
        Args:
            member_id: ID của thành viên
            book_ids: Danh sách ID các sách cần mượn
            days: Số ngày cho mượn (mặc định 14 ngày)
        Returns:
            tuple: (success, message, borrowing_id)
        """
        try:
            with transaction.atomic():
                # Kiểm tra thành viên
                member = Member.objects.get(member_id=member_id)
                if not member.is_active():
                    return False, "Thành viên không hoạt động hoặc đã hết hạn", None
                
                # Kiểm tra sách có sẵn
                books = []
                for book_id in book_ids:
                    book = Book.objects.get(book_id=book_id)
                    if not book.is_available():
                        return False, f"Sách '{book.title}' không có sẵn", None
                    books.append(book)
                
                # Tạo phiếu mượn
                due_date = timezone.now().date() + timedelta(days=days)
                borrowing = Borrowing.objects.create(
                    member=member,
                    due_date=due_date
                )
                
                # Tạo chi tiết phiếu mượn và cập nhật số lượng sách
                for book in books:
                    BorrowingDetail.objects.create(
                        borrowing=borrowing,
                        book=book,
                        quantity=1
                    )
                    book.available_quantity -= 1
                    book.save()
                
                # Ghi log
                Log.objects.create(
                    user_id=member.member_id,
                    user_type='member',
                    action='borrow_book',
                    details=f"Mượn {len(books)} cuốn sách: {', '.join([book.title for book in books])}"
                )
                
                return True, "Mượn sách thành công", borrowing.borrowing_id
                
        except Member.DoesNotExist:
            return False, "Không tìm thấy thành viên", None
        except Book.DoesNotExist:
            return False, "Không tìm thấy sách", None
        except Exception as e:
            return False, f"Lỗi: {str(e)}", None
    
    @staticmethod
    def return_book(borrowing_id, book_ids=None):
        """
        Trả sách
        Args:
            borrowing_id: ID phiếu mượn
            book_ids: Danh sách ID sách cần trả (None = trả tất cả)
        Returns:
            tuple: (success, message, fine_amount)
        """
        try:
            with transaction.atomic():
                borrowing = Borrowing.objects.get(borrowing_id=borrowing_id)
                
                if borrowing.status == 'returned':
                    return False, "Phiếu mượn đã được trả", 0
                
                # Lấy danh sách sách cần trả
                if book_ids is None:
                    details = BorrowingDetail.objects.filter(
                        borrowing=borrowing, 
                        status='borrowed'
                    )
                else:
                    details = BorrowingDetail.objects.filter(
                        borrowing=borrowing, 
                        book__book_id__in=book_ids,
                        status='borrowed'
                    )
                
                if not details.exists():
                    return False, "Không có sách nào để trả", 0
                
                fine_amount = 0
                current_date = timezone.now().date()
                
                # Kiểm tra trả muộn
                if current_date > borrowing.due_date:
                    overdue_days = (current_date - borrowing.due_date).days
                    fine_amount = overdue_days * 5000  # 5000đ/ngày
                
                # Cập nhật chi tiết phiếu mượn và số lượng sách
                for detail in details:
                    detail.status = 'returned'
                    detail.save()
                    
                    book = detail.book
                    book.available_quantity += detail.quantity
                    book.save()
                
                # Kiểm tra xem tất cả sách đã được trả chưa
                remaining_borrowed = BorrowingDetail.objects.filter(
                    borrowing=borrowing,
                    status='borrowed'
                ).count()
                
                if remaining_borrowed == 0:
                    borrowing.status = 'returned'
                    borrowing.return_date = current_date
                    
                    # Tạo phạt nếu trả muộn
                    if fine_amount > 0:
                        Fine.objects.create(
                            borrowing=borrowing,
                            amount=fine_amount,
                            reason='late_return'
                        )
                        borrowing.fine_amount = fine_amount
                
                borrowing.save()
                
                # Ghi log
                returned_books = [detail.book.title for detail in details]
                Log.objects.create(
                    user_id=borrowing.member.member_id,
                    user_type='member',
                    action='return_book',
                    details=f"Trả {len(returned_books)} cuốn sách: {', '.join(returned_books)}"
                )
                
                return True, "Trả sách thành công", fine_amount
                
        except Borrowing.DoesNotExist:
            return False, "Không tìm thấy phiếu mượn", 0
        except Exception as e:
            return False, f"Lỗi: {str(e)}", 0
    
    @staticmethod
    def check_overdue_books():
        """
        Kiểm tra và cập nhật trạng thái sách quá hạn
        Returns:
            list: Danh sách phiếu mượn quá hạn
        """
        current_date = timezone.now().date()
        overdue_borrowings = Borrowing.objects.filter(
            due_date__lt=current_date,
            status='borrowed'
        )
        
        for borrowing in overdue_borrowings:
            borrowing.status = 'overdue'
            borrowing.save()
        
        return list(overdue_borrowings)
    
    @staticmethod
    def calculate_fine(borrowing_id):
        """
        Tính tiền phạt cho phiếu mượn
        Args:
            borrowing_id: ID phiếu mượn
        Returns:
            decimal: Số tiền phạt
        """
        try:
            borrowing = Borrowing.objects.get(borrowing_id=borrowing_id)
            current_date = timezone.now().date()
            
            if borrowing.status == 'returned':
                return 0
            
            if current_date > borrowing.due_date:
                overdue_days = (current_date - borrowing.due_date).days
                return overdue_days * 5000  # 5000đ/ngày
            
            return 0
        except Borrowing.DoesNotExist:
            return 0
    
    @staticmethod
    def get_member_borrowing_history(member_id):
        """
        Lấy lịch sử mượn sách của thành viên
        Args:
            member_id: ID thành viên
        Returns:
            QuerySet: Danh sách phiếu mượn
        """
        try:
            member = Member.objects.get(member_id=member_id)
            return Borrowing.objects.filter(member=member).order_by('-borrow_date')
        except Member.DoesNotExist:
            return Borrowing.objects.none()
    
    @staticmethod
    def search_books(query):
        """
        Tìm kiếm sách
        Args:
            query: Từ khóa tìm kiếm
        Returns:
            QuerySet: Danh sách sách
        """
        return Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__name__icontains=query) |
            Q(isbn__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()
    
    @staticmethod
    def get_popular_books(limit=10):
        """
        Lấy danh sách sách phổ biến (được mượn nhiều nhất)
        Args:
            limit: Số lượng sách giới hạn
        Returns:
            QuerySet: Danh sách sách phổ biến
        """
        from django.db.models import Count
        
        return Book.objects.annotate(
            borrow_count=Count('borrowingdetail')
        ).order_by('-borrow_count')[:limit]
