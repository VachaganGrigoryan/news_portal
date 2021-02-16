from django.conf import settings
from django.template import Library

from categories.models import Menu, Category

register = Library()


@register.inclusion_tag("menu.html")
def menu(site_menu=None, path=None):
    main_menu = Menu.objects.filter(name=site_menu).first() if site_menu in settings.DEFAULT_MENUS else []
    menu_items = Category.objects.filter(menu=main_menu.id) if main_menu else []
    return {"menu_items": menu_items, "path": path}
