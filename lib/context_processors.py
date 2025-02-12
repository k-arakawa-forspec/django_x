from django.conf import settings

def set_cookie(request):
    if request.COOKIES.get('colorMode') is None:
        return {
            'colorMode': settings.DEFAULT_COLOR_MODE
        }
    return {
        'colorMode': request.COOKIES.get('colorMode')
    }
