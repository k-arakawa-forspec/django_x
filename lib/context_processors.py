def theme(request):
    return {
        'theme': 'dark' if request.COOKIES.get('is_dark_theme') == 'True' else 'light'
    }
