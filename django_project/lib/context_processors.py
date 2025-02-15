from django.conf import settings
from django.http import HttpRequest

def fetch_color_mode(request):
    return {
        'color_mode': request.COOKIES.get('color_mode')
    }