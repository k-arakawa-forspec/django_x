from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Post

# Create your views here.
class IndexView(ListView):
    template_name = "home/index.html"

    # 投稿のユーザを外部キーとしてprofileオブジェクトを取得する
    # ポスト主のフォロワーがログインユーザである（＝ログインユーザがフォローしているポスト）ことを条件にフィルタリング
    def get_queryset(self):
        queryset = Post.objects.select_related('user__profile').filter(user__follower_user_set=self.request.user).order_by('-created_at')
        return queryset