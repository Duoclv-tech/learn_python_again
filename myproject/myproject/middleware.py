from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect

class AutoLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and '/admin' in request.path:
            # Get or create a default superuser
            user, created = User.objects.get_or_create(
                username='admin',
                defaults={
                    'is_staff': True,
                    'is_superuser': True,
                    'email': 'admin@example.com'
                }
            )
            
            if created:
                user.set_password('admin123')
                user.save()
            
            # Tự động đăng nhập
            login(request, user)
            
            # Nếu đang ở trang login, chuyển hướng về trang chính của admin
            if request.path == '/admin/login/':
                return redirect('/admin/')
        
        response = self.get_response(request)
        return response
