def settings(request):
  color_mode = request.COOKIES.get('color_mode', 'light')

  return {
    'color_mode': color_mode,
  }
