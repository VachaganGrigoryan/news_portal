from django.conf import settings
from django.db import models
from django.db.models import JSONField
from django.urls import reverse
from django.utils.text import slugify

from blog.utils import slug_logic


class Menu(models.Model):
    name = models.CharField(max_length=128, choices=settings.DEFAULT_MENUS.items(), unique=True)
    json_content = JSONField(blank=True, default=dict, editable=False)

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(editable=False, unique=True)
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name_plural = 'categories'

    def __str__(self):
        model_path = [self.name]
        item = self.parent
        while item is not None:
            model_path.append(item.name)
            item = item.parent

        return ' -> '.join(reversed(model_path))

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('category-detail', kwargs=kwargs)

    def get_unique_slug(self):
        self.slug = slugify(self.name, allow_unicode=True)
        slug_logic(self, 0)

    def save(self, *args, **kwargs):
        self.get_unique_slug()
        super(Category, self).save(*args, **kwargs)

