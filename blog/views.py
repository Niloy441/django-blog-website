from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def home(request):
    posts = Post.objects.all().order_by('-created_date')[:5]
    return render(request, 'blog/home.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_date')
    liked = False
    if request.user.is_authenticated:
        liked = Like.objects.filter(post=post, user=request.user).exists()
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added.')
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'liked': liked,
    })

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Create Post'})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, 'You are not allowed to edit this post.')
        return redirect('post_detail', pk=post.pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Edit Post'})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, 'You are not allowed to delete this post.')
        return redirect('post_detail', pk=post.pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

@login_required
@require_POST
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    return JsonResponse({'liked': liked, 'total_likes': post.total_likes()})