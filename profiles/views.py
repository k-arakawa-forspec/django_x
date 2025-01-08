from django.urls.base import reverse
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from . import forms
from profiles.forms import ProfileForm
from .models import Profile

# Create your views here.
class DetailView(DetailView):
  template_name = "profiles/detail.html"
  model = Profile

class DetailLoginUserView(DetailView):
  template_name = "profiles/detail.html"

  """
  URL上に `pk` パラメータを設けられないため
  get_object() をオーバーライドして直接取得
  """
  def get_object(self):
    return Profile.objects.get(user=self.request.user)

class UpdateLoginUserView(UpdateView):
  form_class = forms.ProfileForm
  template_name = "profiles/update_login_user.html"

  """
  URL上に `pk` パラメータを設けられないため
  get_object() をオーバーライドして直接取得
  """
  def get_object(self):
    return Profile.objects.get(user=self.request.user)

  def get_success_url(self):
    return reverse('profiles:detail_login_user')

  def upload_file(request):
    #params = {
    #  'upload_form':ProfileForm(),
    #  'id':None,
    #}

    #POSTメソッドでリクエストされた場合
    if request.method == 'POST':
      form = ProfileForm(request.POST, request.FILES)
      #フォームインスタンス作成、POSTデータと画像ファイルをバインド
      if form.is_valid():
        #フォームのデータが有効の場合はDBに保存する
        form.save()
        # フォームに保存する

        #upload_image = form.save()
        #params['id'] = upload_image.login_id
        #画像に対してログインIDを持たせる

        return render(request, 'detail_login_user.html')
        #return render(request, 'detail_login_user.html', params)
    else:
      form = ProfileForm()
    return render(request, 'update_login_user.html',{'form':form})

