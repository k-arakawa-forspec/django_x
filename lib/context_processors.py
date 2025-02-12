from django.conf import settings
from django.http import HttpRequest

def set_cookie(request):
    if request.COOKIES.get('color_mode') is None:
        return {
            'color_mode': settings.DEFAULT_COLOR_MODE
        }
    return {
        'color_mode': request.COOKIES.get('color_mode')
    }