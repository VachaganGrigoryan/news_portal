from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from tinymce.models import HTMLField

from blog.utils import slug_logic
from categories.models import Category


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=120)
    categories = models.ManyToManyField(Category)
    content = HTMLField('Content')
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False, )
    slug = models.SlugField(editable=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('post-detail', kwargs=kwargs)

    def get_unique_slug(self):
        self.slug = slugify(self.title, allow_unicode=True)
        slug_logic(self, 0)

    def save(self, *args, **kwargs):
        self.get_unique_slug()
        super(Post, self).save(*args, **kwargs)
