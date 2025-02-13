def is_dark_theme(request):
    return {'is_dark_theme': request.COOKIES.get('is_dark_theme')}
