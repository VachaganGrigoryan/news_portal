from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Post


def home(request):
    post_list = Post.objects.order_by('-publish')
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 10)
    try:
        latest_post_list = paginator.page(page)
    except PageNotAnInteger:
        latest_post_list = paginator.page(1)
    except EmptyPage:
        latest_post_list = paginator.page(paginator.num_pages)

    template = loader.get_template('home.html')
    context = {
        'post_list': latest_post_list,
    }

    return HttpResponse(template.render(context, request))


def post_detail(request, pk: int, slug: str):
    post = get_object_or_404(Post, pk=pk)

    template = loader.get_template('blog/detail.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))

