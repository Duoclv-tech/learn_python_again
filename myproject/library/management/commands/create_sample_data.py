from django.core.management.base import BaseCommand
from library.sample_data import create_sample_data


class Command(BaseCommand):
    help = 'Tạo dữ liệu mẫu cho hệ thống quản lý thư viện'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Bắt đầu tạo dữ liệu mẫu...')
        )
        
        try:
            create_sample_data()
            self.stdout.write(
                self.style.SUCCESS('Đã tạo dữ liệu mẫu thành công!')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Lỗi khi tạo dữ liệu mẫu: {e}')
            )
