from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from categories.models import Category
from blog.models import Post


def category_detail(request, pk: int, slug: str):
    category = get_object_or_404(Category, pk=pk, slug=slug)
    post_list = Post.objects.filter(categories=pk).order_by('-publish')
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 10)
    try:
        latest_post_list = paginator.page(page)
    except PageNotAnInteger:
        latest_post_list = paginator.page(1)
    except EmptyPage:
        latest_post_list = paginator.page(paginator.num_pages)

    template = loader.get_template('categories/detail.html')
    context = {
        'category': category,
        'post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))


