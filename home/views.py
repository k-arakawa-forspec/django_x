from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from posts.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class ndexView(TemplateView):
    template_name = "home/index.html"
    context_object_name = "posts"
    paginate_by = 10  # 一旦1ページに10件表示

    def get_queryset(self):
        """ フォローしているユーザーの投稿を取得（投稿降順） """
        user = self.request.user
        if user.is_authenticated:
            return Post.objects.filter(user__in=user.get_following_users()).select_related("user").order_by("-created_at")
        return Post.objects.none()  # 未ログインなら空
