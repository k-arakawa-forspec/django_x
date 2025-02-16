def fetch_color_mode(request):
    return {
        'color_mode': request.COOKIES.get('color_mode')
    }