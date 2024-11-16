from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Follow
from django.contrib.auth.models import User

@login_required
def add_follow(request, user):
    followed_user = get_object_or_404(User, pk=user)
    
    # 自分自身をフォローすることはできない
    if followed_user == request.user:
        return HttpResponseForbidden("You cannot follow yourself.")
    
    # すでにフォローしている場合は何もしない
    if Follow.objects.filter(follower=request.user, followed=followed_user).exists():
        return redirect('users:profile', login_id=followed_user.username)
    
    # フォローを作成
    Follow.objects.create(follower=request.user, followed=followed_user)
    
    return redirect('users:profile', login_id=followed_user.username)

@login_required
def remove_follow(request, user):
    followed_user = get_object_or_404(User, pk=user)
    
    # 自分自身をフォロー解除することはできない
    if followed_user == request.user:
        return HttpResponseForbidden("You cannot unfollow yourself.")
    
    # フォロー解除
    follow = Follow.objects.filter(follower=request.user, followed=followed_user).first()
    if follow:
        follow.delete()

    return redirect('users:profile', login_id=followed_user.username)
