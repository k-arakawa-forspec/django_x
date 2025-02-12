from datetime import timedelta
from django.shortcuts import redirect

def button_action(request):
    # クッキーが設定されていない場合
    if request.COOKIES.get('colorMode') is None:
        # 最初にページに訪れたときはクッキーを設定してリダイレクト
        color_mode = 'light'
        response = redirect('accounts:home')  # 現在のページにリダイレクト
        response.set_cookie('colorMode', color_mode, max_age=timedelta(days=30), secure=True, httponly=True)  # クッキー設定
        return response
    else:
        # クッキーが設定されている場合、現在のモードを反転させる
        current_mode = request.COOKIES.get('colorMode')
        color_mode = 'light' if current_mode == 'dark' else 'dark'
        
        # モードを反転させて、リダイレクトなしでクッキーを更新
        response = redirect('accounts:home')  # 現在のページにリダイレクト
        response.set_cookie('colorMode', color_mode, max_age=timedelta(days=30), secure=True, httponly=True)  # 新しいモードに更新
        return response