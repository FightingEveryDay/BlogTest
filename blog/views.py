from django.shortcuts import render, get_object_or_404
from .models import Post
# import markdown


def index(request):
    # return render(request, 'blog/index.html', context={
    #     'title' : '我的博客首页',
    #     'welcome' : '欢迎访问我的博客首页',
    # })
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    # post.body = markdown.markdown(post.body,
    #                               extensions = [
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])
    return render(request, 'blog/detail.html', context={'post':post})


def get_client_ip(request): # 获取ip
    try:
        real_ip = request.META['HTTP_X_FORWARDED_FOR']
        regip = real_ip.split(",")[0]
    except:

        try:
            regip = request.META['REMOTE_ADDR']
        except:
            regip = ""

    return regip