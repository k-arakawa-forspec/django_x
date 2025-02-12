def settings(request):
  color_mode = request.COOKIES.get('color_mode')

  return {
    'color_mode': color_mode,
  }
