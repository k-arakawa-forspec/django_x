from django.views.generic import CreateView, ListView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from . import forms
from .models import Post


# Create your views here.
class CreateView(CreateView):
  form_class = forms.PostForm
  template_name = "posts/create.html"
  success_url = reverse_lazy("accounts:home")

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class IndexView(TemplateView):
  template_name = "posts/list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    post_list = Post.objects.all()
    context["post_list"] = post_list
    return context


class ListView(ListView):
  template_name = "posts/list.html"

  """ (1) ListView のクラス変数 model を指定するケース
  model = Post

  # contextに格納される名前をデフォルトの"object_list"から変更
  context_object_name = 'post_list'
  """

  """ (2) ListView のクラス変数 queryset を指定するケース
  # クラス変数のため静的な指定のみ。
  # 動的な指定(例: リクエスト内容に応じた絞込み)をしたい場合は
  # get_queryset() のオーバーライドを用いる必要がある。
  queryset = Post.objects.all()
  """

  """ (3) ListView のメソッド get_queryset() をオーバーライドするケース """
  model = Post

  def get_queryset(self):
    queryset = super().get_queryset()
    queryset = queryset.all()
    return queryset
