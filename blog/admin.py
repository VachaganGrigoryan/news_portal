from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from blog.models import Post
# from categories.models import CategoryPost


# class CategoryPostAdmin(admin.TabularInline):
#     model = CategoryPost
#     extra = 1
#
#
# class PostAdmin(admin.ModelAdmin):
#     inlines = (CategoryPostAdmin,)


admin.site.register(Post)  # PostAdmin
