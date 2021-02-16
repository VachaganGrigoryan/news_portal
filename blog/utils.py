

def slug_logic(self, i):
    ModelClass = self.__class__
    slug_filter = ModelClass.objects.filter(slug__exact=self.slug)
    if len(slug_filter) == 1:
        if not slug_filter[0].pk == self.pk:
            self.slug = f"{self.slug}-{i}"
            slug_logic(self, i + 1)
