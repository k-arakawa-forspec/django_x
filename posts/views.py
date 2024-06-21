from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms
from .models import Post


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    ordering = ["-id"]
    title = "ポスト一覧"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class MeView(PostListView):
    title = "マイポスト一覧"

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user.id)


class PostCreateView(CreateView):
    form_class = forms.PostForm
    template_name = "posts/create.html"
    success_url = reverse_lazy("accounts:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
