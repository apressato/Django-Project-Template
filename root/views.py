from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'app/home.html')


def internal_server_error_500(request):
    return render(request, 'errors/500.html')


def not_found_404(request, exception):
    return render(request, 'errors/404.html')